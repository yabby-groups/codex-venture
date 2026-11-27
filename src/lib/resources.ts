import { getCollection } from 'astro:content';
import { storyUrl, type Story } from './content';
import { sections, topicLink } from './navigation';
import { repositorySnapshot } from './repositories';
import { resourceTypes, type ResourceType } from './resource-schema';

export const resourcePageSize = 12;
export const resourceBase = (type: ResourceType) => topicLink(type).href;
export const resourceInLearn = (type: ResourceType) => type === 'prompts' || type === 'workflows';
export const resourceSection = (type: ResourceType) => resourceInLearn(type) ? sections.learn : sections.discover;
export const resourcePage = (type: ResourceType, page: number) =>
  page === 1 ? resourceBase(type) : `${resourceBase(type)}page/${page}/`;

export const directoryTitle = (type: ResourceType) => topicLink(type).label;

const profiles = (await getCollection('resources')).map(({ id, data }) => {
  if (id !== data.id) throw new Error(`Resource filename differs from ID: ${id}`);
  return data;
});

export function resourceCatalog(stories: Story[]) {
  const related = Map.groupBy(stories.flatMap((story) =>
    (story.data.resourceIds ?? []).map((id) => ({ id, story }))), ({ id }) => id);
  const ids = new Set(profiles.map(({ id }) => id));
  const routes = new Set(stories.map(storyUrl));
  for (const id of related.keys()) {
    if (!ids.has(id)) throw new Error(`Unknown resource relation: ${id}`);
  }
  const resources = profiles.map((resource) => {
    const matches = (related.get(resource.id) ?? []).map(({ story }) => story);
    const github = resource.type === 'open-source' ? repositorySnapshot(resource.repository) : undefined;
    if (resource.detail && !routes.has(resource.detail)) throw new Error(`Unknown resource detail: ${resource.id}`);
    return {
      ...resource, github,
      license: resource.license ?? (github?.license === 'NOASSERTION' ? undefined : github?.license ?? undefined),
      detail: resource.detail ?? resource.site, verified: resource.verifiedAt, added: resource.addedAt,
      tags: [...new Set([...resource.tags, ...matches.flatMap((story) => story.data.tags)])],
      articles: [...new Set(matches.map(storyUrl))],
    };
  });
  const identities = new Set<string>();
  for (const row of resources) {
    const url = new URL(row.site);
    url.hash = '';
    const identity = row.type + ':' + url.href.replace(/\/$/, '');
    if (identities.has(identity)) throw new Error(`Duplicate resource source: ${row.id}`);
    identities.add(identity);
  }
  return resources.sort((a, b) => b.added.localeCompare(a.added) || a.id.localeCompare(b.id));
}

export type Resource = ReturnType<typeof resourceCatalog>[number];
export const resourceSearchText = (row: Resource) =>
  [row.name, row.nameZh, ...row.summary, row.repository, row.site, ...row.platforms,
    ...row.tags, ...row.categories.flat()].filter(Boolean).join(' ').normalize('NFKC').toLowerCase();

export const resourceDate = (row: Resource) => row.updatedAt ?? row.added;
export const resourceDirectories = (stories: Story[]) => {
  const resources = Map.groupBy(resourceCatalog(stories), (resource) => resource.type);
  return resourceTypes.map((type) => ({ type, rows: resources.get(type) ?? [] }));
};
