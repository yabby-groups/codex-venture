import { allStories, dateKey } from '../lib/content';
import { resourceCatalog } from '../lib/resources';

export async function GET() {
  const articles = await allStories();
  const resources = resourceCatalog(articles);
  const count = <T>(rows: T[], key: (row: T) => string) =>
    Object.fromEntries([...Map.groupBy(rows, key)].map(([name, group]) => [name, group.length]));
  const latest = [
    articles[0] && dateKey(articles[0].data.published),
    ...resources.map((resource) => resource.updatedAt ?? resource.addedAt),
  ].filter(Boolean).sort().at(-1);
  return Response.json({
    latest,
    articles: count(articles, (story) => story.data.type ?? story.collection),
    categories: count(articles, (story) => story.data.category),
    resources: count(resources, (resource) => resource.type),
  });
}
