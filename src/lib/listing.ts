import { resourceDirectories } from './resources';
import { categories, hubs, isWeekly, types, type Story } from './content';

export const pageSize = 20;

export const listingSections = (stories: Story[]) => {
const directoryKeys = new Set<string>(resourceDirectories(stories).map(({ type }) => type));
return [
  { base: '/news/', zh: '最新资讯', en: 'Latest News', stories: stories.filter((story) => story.collection === 'news' && (!story.data.type || ['news', 'models'].includes(story.data.type))) },
  { base: '/daily/', zh: '每日 AI 简报', en: 'Daily AI Briefing',
    byDate: true,
    stories: stories.filter((story) => story.collection === 'daily' && !isWeekly(story)) },
  { base: '/weekly/', zh: '每周精选', en: 'Weekly Review',
    stories: stories.filter(isWeekly) },
  ...Object.entries(hubs).map(([key, [zh, en]]) => ({
    base: `/${key}/`, zh, en,
    topics: Object.entries(types).filter(([id, [, , hub]]) => hub === key && stories.some(({ data }) => data.type === id)),
    stories: stories.filter(({ data }) => data.type && types[data.type][2] === key),
  })),
  ...Object.entries(types).filter(([key]) => key !== 'news' && !directoryKeys.has(key)).map(([key, [zh, en]]) => ({
    base: `/topics/${key}/`, zh, en,
    stories: stories.filter((story) => story.collection === 'news' &&
      (story.data.type ?? (story.data.category === 'models' ? 'models' : 'news')) === key),
  })).filter(({ stories }) => stories.length),
  ...Object.entries(categories).filter(([key]) => key !== 'briefing').map(([key, [zh, en]]) => ({
    base: `/category/${key}/`, zh, en,
    stories: stories.filter((story) => story.data.category === key),
  })),
];
};
