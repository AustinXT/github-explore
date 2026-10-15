"""Shared calendar rules: seven UTC dates ending on the issue date, inclusive."""
from datetime import date, timedelta


def period(issue_date: str) -> dict[str, str]:
    end = date.fromisoformat(issue_date)
    if end.isoformat() != issue_date:
        raise ValueError("issue date must be YYYY-MM-DD")
    start = end - timedelta(days=6)
    year, week, _ = end.isocalendar()
    return {
        "week": f"{year}-W{week:02d}",
        "window_start": start.isoformat(),
        "window_end": end.isoformat(),
        "since": (start - timedelta(days=1)).isoformat(),
        "after_date": (start - timedelta(days=1)).isoformat(),
        "before_date": (end + timedelta(days=1)).isoformat(),
    }
