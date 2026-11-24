import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { allStories, storyUrl } from '../lib/content';

export async function GET({ site }: APIContext) {
  return rss({
    title: 'Codex Venture',
    description: '全球 AI 资讯 · Global AI News',
    site: site!,
    customData: '<language>zh-CN</language>',
    items: (await allStories()).slice(0, 40).map((story) => ({
      title: story.data.titleZh + ' / ' + story.data.titleEn,
      description: story.data.summaryZh + '\n' + story.data.summaryEn,
      pubDate: story.data.published,
      link: storyUrl(story),
      categories: story.data.tags,
    })),
  });
}
