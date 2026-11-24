import { categories, isWeekly, type Story } from './content';

export const pageSize = 20;

export const listingSections = (stories: Story[]) => [
  { base: '/news/', zh: '最新资讯', en: 'Latest News', stories: stories.filter((story) => story.collection === 'news') },
  { base: '/daily/', zh: '每日 AI 简报', en: 'Daily AI Briefing',
    intro: ['按日期阅读全球 AI 技术动态。', 'Follow global AI developments by date.'],
    stories: stories.filter((story) => story.collection === 'daily' && !isWeekly(story)) },
  { base: '/weekly/', zh: '每周精选', en: 'Weekly Review',
    intro: ['回顾值得持续关注的 AI 技术进展。', 'Revisit the AI developments worth following.'],
    stories: stories.filter(isWeekly) },
  ...Object.entries(categories).filter(([key]) => key !== 'briefing').map(([key, [zh, en]]) => ({
    base: `/category/${key}/`, zh, en,
    stories: stories.filter((story) => story.data.category === key),
  })),
];
