import type { APIRoute } from 'astro';
import { entities, entityUrl } from '../lib/entities';

export const GET: APIRoute = ({ site }) => {
  const link = (title: string, path: string) => `- [${title}](${new URL(path, site).href})`;
  const sections = [
    ['Editorial policy and sources', '/editorial/'], ['Skills', '/topics/skills/'],
    ['Plugins', '/topics/plugins/'], ['MCP integrations', '/topics/mcp/'],
    ['Tutorials', '/topics/tutorials/'], ['Workflows', '/topics/workflows/'],
    ['Usage stories', '/topics/stories/'], ['Building in public', '/topics/building-in-public/'],
    ['RSS', '/rss.xml'], ['Sitemap', '/sitemap-index.xml'], ['Public entity index', '/entities.json'],
  ];
  return new Response([
    '# Codex Venture', '',
    '> Independent coverage of global AI technology in Simplified Chinese and English. No official affiliation with OpenAI.', '',
    '## Sections and resources', '', ...sections.map(([title, path]) => link(title, path)), '',
    '## Technology topics', '', ...entities.map((entity) => link(entity.name, entityUrl(entity))), '',
  ].join('\n'), { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
