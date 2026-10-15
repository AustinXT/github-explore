"""Weekly window, history, deduplication, and workflow regressions."""
import io
import re
import subprocess
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src/scripts"))
import collect_weekly_facts as collect
import dedup_weekly as dedup
import record_weekly as record
from weekly_period import period

TYPE = next(iter(record.VALID_TYPES))


class WeeklyTests(unittest.TestCase):
    def test_seven_days_across_year(self):
        window = period("2027-01-03")
        self.assertEqual(window["week"], "2026-W53")
        self.assertEqual(window["window_start"], "2026-12-28")
        self.assertEqual(window["after_date"], "2026-12-27")
        self.assertEqual(window["before_date"], "2027-01-04")

    def test_same_week_rerun_and_next_week(self):
        with tempfile.TemporaryDirectory() as folder, redirect_stdout(io.StringIO()):
            out = Path(folder) / "index.jsonl"
            for day in ["2026-10-12", "2026-10-18", "2026-10-19"]:
                self.assertEqual(record.main(["--type", TYPE, "--date", day,
                    "--slug", day, "--title", "Weekly", "--out", str(out)]), 0)
            rows = [json.loads(line) for line in out.read_text().splitlines()]
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["window_start"], "2026-10-06")
            self.assertEqual(rows[1]["week"], "2026-W43")

    def test_check_has_no_write_side_effect(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder) / "index.jsonl"
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                self.assertEqual(record.main(["--type", TYPE, "--date", "2026-10-18",
                    "--check", "--out", str(out)]), 0)
            self.assertEqual(stdout.getvalue().strip(), "false")
            self.assertFalse(out.exists())

    def test_dedup_expiration_and_future_entries(self):
        cache = {"meta": {"window_days": 30}, "entries": [
            {"date_seen": "2026-09-17"}, {"date_seen": "2026-09-18"},
            {"date_seen": "2026-10-18"}, {"date_seen": "2026-10-19"}]}
        self.assertEqual(dedup._prune(cache, "2026-10-18"), 2)
        self.assertEqual(len(cache["entries"]), 2)
        self.assertEqual(dedup.normalize_url("https://arxiv.org/pdf/2601.00001v2.pdf"),
                         dedup.normalize_url("https://arxiv.org/abs/2601.00001"))

    def test_workflow_schedule_and_guard(self):
        import yaml
        # BaseLoader avoids YAML 1.1 interpreting 'on' as a boolean key.
        workflow = yaml.load((ROOT / ".github/workflows/weekly-digest.yml").read_text(), Loader=yaml.BaseLoader)
        self.assertEqual(workflow["on"]["schedule"][0]["cron"], "0 22 * * 4")
        steps = workflow["jobs"]["digest"]["steps"]
        generation = next(s for s in steps if s.get("name", "").startswith("生成周刊"))
        self.assertIn("steps.issue.outputs.exists", generation["if"])
        self.assertNotIn("matrix", workflow["jobs"]["digest"])
        for step in steps:
            if "run" in step:
                shell = re.sub(r"\$\{\{.*?\}\}", "placeholder", step["run"], flags=re.S)
                checked = subprocess.run(["bash", "-n"], input=shell, text=True, capture_output=True)
                self.assertEqual(checked.returncode, 0, checked.stderr)



if TYPE == "ecosystem":
    class EcosystemTests(unittest.TestCase):
        def test_trending_window_aggregation_and_stale_data(self):
            def row(day, name="org/repo", rank=5):
                return {"period_type": "daily", "period_key": day, "name": name,
                        "url": f"https://github.com/{name}", "rank": rank}
            rows = [row("2026-10-11", rank=10), row("2026-10-12", rank=3),
                    row("2026-10-12", rank=3), row("2026-10-18", rank=2),
                    row("2026-10-19", "future/repo"), row("2026-10-01", "old/repo")]
            with tempfile.TemporaryDirectory() as folder:
                source = Path(folder) / "snapshots.jsonl"
                source.write_text("\n".join(json.dumps(r) for r in rows))
                with patch.object(collect, "TRENDING_SNAPSHOTS", source):
                    result, _ = collect.load_rising_repos("2026-10-18", {}, lambda *_: True)
                    self.assertEqual(len(result), 1)
                    self.assertEqual(result[0]["trending_days"], 2)
                    self.assertEqual(result[0]["rank_delta"], 8)
                    self.assertEqual(result[0]["rank"], 2)
                    empty, _ = collect.load_rising_repos("2026-11-01", {}, lambda *_: True)
                    self.assertEqual(empty, [])

        def test_facts_cache_ignores_expired_and_future_items(self):
            cache = {"entries": [{"key": "old", "date_seen": "2026-08-01"},
                                 {"key": "current", "date_seen": "2026-10-12"},
                                 {"key": "future", "date_seen": "2026-10-19"}]}
            with patch.object(collect, "_load_json", return_value=cache):
                self.assertEqual(collect.load_cache_seen_keys("ecosystem", "2026-10-18"), ["current"])

        def test_star_window_is_bounded_and_aggregated(self):
            items = [{"name": "o/" + name, "url": "https://github.com/o/" + name,
                      "starredAt": stamp} for name, stamp in [
                ("old", "2026-10-11T23:59:59Z"), ("start", "2026-10-12T00:00:00Z"),
                ("end", "2026-10-18T23:59:59Z"), ("future", "2026-10-19T00:00:00Z")]]
            data = {"users": [{"login": "a", "items": items}, {"login": "b", "items": items}]}
            with patch.object(collect, "_load_json", return_value=data):
                result = collect.load_new_pro_stars("2026-10-11", "2026-10-18", {}, lambda *_: True)
            self.assertEqual({r["name"] for r in result}, {"o/start", "o/end"})
            self.assertTrue(all(r["star_users"] == 2 for r in result))


if __name__ == "__main__":
    unittest.main()
