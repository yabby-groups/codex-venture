import curation from '../../config/editorial-curation.json';
import type { Story } from './content';

const articles: Record<string, { decision: string; recommendation?: string }> = curation.articles;

export const onEditorialDesk = (story: Story) =>
  story.data.status !== 'archived' && (story.collection !== 'news' || articles[story.id]?.decision !== 'ARCHIVE');

export function recommendations(stories: Story[]) {
  const candidates = stories.filter((story) => story.collection === 'news' && onEditorialDesk(story))
    .map((story) => ({
      story,
      tier: articles[story.id]?.recommendation ?? story.data.editorial?.tier,
      score: story.data.editorial?.score,
    }))
    .filter(({ tier }) => tier === 'lead' || tier === 'featured')
    .sort((a, b) => Number(b.tier === 'lead') - Number(a.tier === 'lead') ||
      (b.score ?? 0) - (a.score ?? 0));
  const picks: Story[] = [];
  const hosts = new Set<string>();
  const topics = new Map<string, number>();
  const types = new Map<string, number>();
  for (const { story } of candidates) {
    const host = new URL(story.data.sources[0].url).hostname;
    const topic = story.data.category;
    const type = story.data.type ?? 'news';
    if (hosts.has(host) || (topics.get(topic) ?? 0) >= 2 || (types.get(type) ?? 0) >= 2 ||
        picks.some((pick) => story.data.project && story.data.project === pick.data.project)) continue;
    picks.push(story);
    hosts.add(host);
    topics.set(topic, (topics.get(topic) ?? 0) + 1);
    types.set(type, (types.get(type) ?? 0) + 1);
    if (picks.length === 4) break;
  }
  return { lead: candidates[0]?.tier === 'lead' ? picks[0] : undefined, picks };
}
