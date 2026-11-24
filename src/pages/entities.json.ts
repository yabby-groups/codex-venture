import type { APIRoute } from 'astro';
import { allStories, storyUrl } from '../lib/content';
import { entities, entityStories, entityUrl, resourceEntityId } from '../lib/entities';

import { resourceCatalog } from '../lib/resources';

export const GET: APIRoute = async ({ site }) => {
  const stories = await allStories();
  const url = (path: string) => new URL(path, site).href;
  const index = entities.map(({ articles, ...entity }) => ({
    ...entity,
    url: url(entityUrl(entity)),
    articles: entityStories({ ...entity, articles }, stories).map((story) => url(storyUrl(story))),
  }));
  const resources = resourceCatalog(stories);
  const resourceIndex = resources.map((row) => ({
    ...row, entityId: resourceEntityId(row.id, site), url: url(row.detail),
    detail: url(row.detail), articles: row.articles.map(url),
  }));
  const updated = ['2026-11-24', ...resources.map((row) => row.verified)].sort().at(-1);
  return new Response(JSON.stringify({ schemaVersion: 1, updated, entities: [...index, ...resourceIndex] }, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
