import type { APIRoute } from 'astro';
import { allStories } from '../lib/content';
import { resourceCatalog, resourceDate, resourceSearchText } from '../lib/resources';

export const GET: APIRoute = async () => Response.json(
  resourceCatalog(await allStories()).map((row) => ({
    name: row.name, nameZh: row.nameZh, type: row.type, detail: row.detail,
    source: row.site, date: resourceDate(row), text: resourceSearchText(row),
  })),
);
