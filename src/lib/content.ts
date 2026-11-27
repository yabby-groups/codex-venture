import { getCollection, type CollectionEntry } from 'astro:content';

import { sections, technologyLink, topicLink } from './navigation';

export type Story = CollectionEntry<'news'> | CollectionEntry<'daily'>;
export const storyUrl = (story: Story) => '/' + story.collection + '/' + story.id + '/';
export const allStories = async () => (await Promise.all([getCollection('news'), getCollection('daily')]))
  .flat().sort((a, b) => b.data.published.getTime() - a.data.published.getTime() || a.id.localeCompare(b.id));
export const dateKey = (date: Date) => new Intl.DateTimeFormat('sv-SE', {
  timeZone: 'Asia/Shanghai', year: 'numeric', month: '2-digit', day: '2-digit',
}).format(date);

export const isWeekly = (story: Story) => story.collection === 'daily' && story.id.startsWith('weekly-');
export const storySection = (story: Story) => story.collection === 'news'
  ? story.data.type && story.data.type !== 'news'
    ? topicLink(story.data.type)
    : technologyLink(story.data.category)
  : isWeekly(story) ? sections.weekly : sections.daily;
