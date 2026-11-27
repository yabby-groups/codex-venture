import { onEditorialDesk } from './editorial';
import { resourceTypes } from './resource-schema';
import { isWeekly, type Story } from './content';
import { hubs, sections, technologyLinks, types } from './navigation';

export const pageSize = 20;

export const listingSections = (stories: Story[]) => {
stories = stories.filter(onEditorialDesk);
const directoryKeys = new Set<string>(resourceTypes);
return [
  { base: sections.news.href, zh: sections.news.label[0], en: sections.news.label[1], stories: stories.filter((story) => story.collection === 'news' && (!story.data.type || ['news', 'models'].includes(story.data.type))) },
  { base: sections.daily.href, zh: sections.daily.label[0], en: sections.daily.label[1],
    byDate: true,
    stories: stories.filter((story) => story.collection === 'daily' && !isWeekly(story)) },
  { base: sections.weekly.href, zh: sections.weekly.label[0], en: sections.weekly.label[1],
    stories: stories.filter(isWeekly) },
  ...Object.entries(hubs).map(([key, [zh, en]]) => ({
    base: sections[key as keyof typeof hubs].href, zh, en,
    topics: Object.entries(types).filter(([id, [, , hub]]) => hub === key && stories.some(({ data }) => data.type === id)),
    stories: stories.filter(({ data }) => data.type && types[data.type][2] === key),
  })),
  ...Object.entries(types).filter(([key]) => key !== 'news' && !directoryKeys.has(key)).map(([key, [zh, en]]) => ({
    base: `/topics/${key}/`, zh, en,
    stories: stories.filter((story) => story.collection === 'news' &&
      (story.data.type ?? (story.data.category === 'models' ? 'models' : 'news')) === key),
  })).filter(({ stories }) => stories.length),
  ...technologyLinks.map(({ href, label: [zh, en] }) => ({
    base: href, zh, en,
    stories: stories.filter((story) => href === `/category/${story.data.category}/`),
  })),
];
};
