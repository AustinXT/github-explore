import rss from "@astrojs/rss";
import type { APIContext } from "astro";
import { getCollection } from "astro:content";
import { SITE, absoluteUrl, getWeeklyDigests } from "~/lib/data";

// 开源周刊专属 RSS。正文用 content collection（frontmatter），元数据兜底用 weekly_digests.jsonl。
export async function GET(_ctx: APIContext) {
  const entries = await getCollection("weekly");
  const metaByDate = new Map(getWeeklyDigests().map((d) => [d.date, d]));

  const items = entries
    .map((e) => {
      const date = (e.data.date as string) ?? e.id.replace(/\.md$/, "");
      const meta = metaByDate.get(date);
      return {
        date,
        title: (e.data.title as string) ?? meta?.title ?? `开源周刊 ${date}`,
        description: (e.data.summary as string) ?? meta?.summary ?? "",
        link: absoluteUrl(`/weekly/${date}`),
        pubDate: /^\d{4}-\d{2}-\d{2}$/.test(date) ? new Date(date) : new Date(),
        categories: (e.data.tags as string[]) ?? ["开源周刊"],
      };
    })
    .sort((a, b) => (a.date > b.date ? -1 : 1))
    .slice(0, 50);

  return rss({
    title: "开源周刊 · GitHub Explorer",
    description: "每周聚合 GitHub Trending、AI 大牛 Star 动态与本站深度报告的开源 AI 生态周刊。",
    site: absoluteUrl("/"),
    items,
    customData: `<language>zh-CN</language>`,
    stylesheet: false,
  });
}
