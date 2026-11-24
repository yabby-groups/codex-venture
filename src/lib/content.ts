import { getCollection, type CollectionEntry } from 'astro:content';

import types from '../../config/content-types.json';
export { types };

export const hubs = {
  discover: ['发现', 'Discover'],
  learn: ['实践', 'Learn'],
  stories: ['故事', 'Stories'],
};

export type Story = CollectionEntry<'news'> | CollectionEntry<'daily'>;
export const categories = {
  models: ['AI 模型', 'AI Models'],
  coding: ['AI 编程', 'AI Coding'],
  image: ['AI 图像', 'AI Image'],
  video: ['AI 视频', 'AI Video'],
  audio: ['AI 音频', 'AI Audio'],
  agents: ['AI Agent', 'AI Agents'],
  'open-source': ['开源 AI', 'Open Source AI'],
  briefing: ['每日 AI 简报', 'Daily AI Briefing'],
};
export const storyUrl = (story: Story) => '/' + story.collection + '/' + story.id + '/';
export const allStories = async () => (await Promise.all([getCollection('news'), getCollection('daily')]))
  .flat().sort((a, b) => b.data.published.getTime() - a.data.published.getTime() || a.id.localeCompare(b.id));
export const dateKey = (date: Date) => new Intl.DateTimeFormat('sv-SE', {
  timeZone: 'Asia/Shanghai', year: 'numeric', month: '2-digit', day: '2-digit',
}).format(date);

export const isWeekly = (story: Story) => story.collection === 'daily' && story.id.startsWith('weekly-');
export const storySection = (story: Story) => story.collection === 'news'
  ? story.data.type && story.data.type !== 'news'
    ? { href: `/topics/${story.data.type}/`, label: types[story.data.type].slice(0, 2) }
    : { href: `/category/${story.data.category}/`, label: categories[story.data.category] }
  : isWeekly(story)
    ? { href: '/weekly/', label: ['每周精选', 'Weekly Review'] }
    : { href: '/daily/', label: ['每日简报', 'Daily Briefing'] };
