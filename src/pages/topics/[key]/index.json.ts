import type { APIRoute } from 'astro';
import { allStories } from '../../../lib/content';
import { resourceDirectories, resourcePageSize, resourceSearchText } from '../../../lib/resources';

export async function getStaticPaths() {
  return resourceDirectories(await allStories()).map(({ type, rows }) => ({
    params: { key: type },
    props: { rows: rows.map((row, index) => ({
      id: row.id, page: Math.floor(index / resourcePageSize) + 1, name: row.name,
      verified: row.verified, releasedAt: row.releasedAt, featured: row.featured, stars: row.github?.stargazers_count,
      facets: {
        platform: row.platforms, category: row.categories.map(([, en]) => en), tag: row.tags,
        license: row.license ? [row.license] : [], install: row.install ? [row.install] : [],
        transport: row.transport ? [row.transport] : [],
      },
      text: resourceSearchText(row),
    })) },
  }));
}
export const GET: APIRoute = ({ props }) => new Response(JSON.stringify(props.rows), {
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
});
