import type { APIRoute } from 'astro';
import { allStories, storyUrl } from '../lib/content';
import { entities, entityStories, entityUrl } from '../lib/entities';

export const GET: APIRoute = async ({ site }) => {
  const stories = await allStories();
  const url = (path: string) => new URL(path, site).href;
  const index = entities.map(({ articles, ...entity }) => ({
    ...entity,
    url: url(entityUrl(entity)),
    articles: entityStories({ ...entity, articles }, stories).map((story) => url(storyUrl(story))),
  }));
  return new Response(JSON.stringify({ schemaVersion: 1, updated: '2026-11-24', entities: index }, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
