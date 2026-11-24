import type { Story } from './content';
import snapshots from './github-snapshots.json';

interface Snapshot {
  stargazers_count: number;
  forks_count: number;
  language?: string;
  license?: string | null;
  pushed_at?: string;
  homepage?: string;
  collected: string;
}

const snapshotsByName: Record<string, Snapshot> = snapshots;

export function repositorySnapshot(repository: string | undefined) {
  if (!repository) return;
  const url = new URL(repository);
  if (url.origin !== 'https://github.com' || !/^\/[\w.-]+\/[\w.-]+\/?$/.test(url.pathname)) return;
  return snapshotsByName[url.pathname.slice(1).replace(/\/$/, '').toLowerCase()];
}

export interface RepositoryInfo {
  name: string;
  snapshot?: Snapshot;
  url: string;
  release?: { label: string; url: string };
}

export function repositoryFor(story: Story): RepositoryInfo | undefined {
  if (story.collection !== 'news') return;
  for (const source of story.data.sources) {
    const url = new URL(source.url);
    if (url.origin !== 'https://github.com') continue;
    const match = url.pathname.match(/^\/([\w.-]+)\/([\w.-]+)(?:\/(releases\/tag\/.+))?\/?$/);
    if (!match || ['orgs', 'topics', 'users', 'sponsors', 'collections', 'marketplace'].includes(match[1])) continue;
    const name = `${match[1]}/${match[2]}`;
    return {
      name,
      snapshot: snapshotsByName[name.toLowerCase()],
      url: `https://github.com/${name}`,
      release: match[3] ? { label: source.title, url: source.url } : undefined,
    };
  }
}
