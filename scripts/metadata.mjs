import { pathToFileURL } from 'node:url';
import { readdirSync, readFileSync } from 'node:fs';
import { parse } from 'yaml';

const types = JSON.parse(readFileSync('config/content-types.json', 'utf8'));

const read = (directory, collection) => readdirSync(directory).filter((name) => name.endsWith('.md')).map((name) => {
  const slug = name.slice(0, -3);
  const text = readFileSync(directory + '/' + name, 'utf8');
  const match = /^---\r?\n([\s\S]+?)\r?\n---\r?\n([\s\S]*)$/.exec(text);
  if (!match || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug)) throw new Error('Invalid article ' + name);
  const [, frontmatter, body] = match;
  const data = parse(frontmatter);
  const textFields = ['titleZh', 'titleEn', 'summaryZh', 'summaryEn'];
  const categories = ['models', 'coding', 'image', 'video', 'audio', 'agents', 'open-source', 'briefing'];
  const slugPattern = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
  if (!data || textFields.some((key) => typeof data[key] !== 'string' || !data[key].trim()) ||
      !categories.includes(data.category) || !Array.isArray(data.tags) || !data.tags.length ||
      data.tags.some((tag) => typeof tag !== 'string' || !slugPattern.test(tag)) ||
      !Array.isArray(data.sources) || !data.sources.length ||
      data.sources.some((source) => typeof source?.title !== 'string' || !source.title.trim() ||
        typeof source.url !== 'string' || !source.url.startsWith('https://')) ||
      typeof data.published !== 'string' ||
      !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$/.test(data.published) ||
      !Number.isFinite(Date.parse(data.published))) throw new Error('Invalid frontmatter in ' + name);
  if (data.type && (collection !== 'news' || !Object.hasOwn(types, data.type) ||
      !/^\d{4}-\d{2}-\d{2}$/.test(data.verified ?? '') ||
      !['current', 'needs-review', 'archived'].includes(data.status) ||
      typeof data.tested !== 'boolean' || typeof data.version !== 'string' || !data.version.trim() ||
      (data.project !== undefined && !slugPattern.test(data.project)) ||
      (['skills', 'plugins', 'mcp', 'open-source', 'tools'].includes(data.type) && !data.project)))
    throw new Error('Invalid content lifecycle metadata in ' + name);
  const blocks = body.trim().split(/\n\s*\n/);
  let pairs = 0;
  for (const block of data.blocks ?? []) {
    if (block.kind === 'code' && block.language === 'json') {
      try { JSON.parse(block.code); }
      catch { throw new Error('Invalid JSON example in ' + name); }
    }
  }
  const zh = '<p lang="zh-CN">';
  const en = '<p lang="en">';
  const han = /\p{Script=Han}/u;
  const latin = /[a-zA-Z]{2}/;
  const textOnly = (html) => html.replace(/<[^>]+>/g, '').replace(/https?:\/\/\S+/g, '').trim();
  const pair = /<span lang="zh-CN">(.+?)<\/span><span lang="en">(.+?)<\/span>/g;
  const balanced = (block) => {
    const matches = [...block.matchAll(pair)];
    return matches.length > 0 && matches.every(([, c, e]) => han.test(textOnly(c)) && latin.test(textOnly(e)));
  };
  for (let i = 0; i < blocks.length; i++) {
    const block = blocks[i].trim();
    if (block.startsWith(zh) && block.endsWith('</p>') && blocks[i + 1]?.startsWith(en) &&
        blocks[i + 1].endsWith('</p>') && han.test(textOnly(block)) && latin.test(textOnly(blocks[i + 1]))) {
      i++;
      pairs++;
    } else if (!(/^(<h2>.*<\/h2>|<ul>[\s\S]*<\/ul>)$/.test(block) && balanced(block))) {
      throw new Error('Invalid bilingual block in ' + name);
    }
  }
  const tags = body.match(/<[^>]*>/g) ?? [];
  const allowed = /^(?:<\/(?:p|h2|ul|li|span|a|strong|em|code)>|<(?:h2|ul|li|strong|em|code)>|<(?:p|span) lang="(?:zh-CN|en)">|<a href="https:\/\/[^\"<>\s]+">)$/;
  if (tags.some((tag) => !allowed.test(tag)) || body.replace(/<[^>]*>/g, '').includes('<'))
    throw new Error('Unsupported markup in ' + name);
  if (!pairs || !han.test(data.titleZh) || !han.test(data.summaryZh) ||
      !latin.test(data.titleEn) || !latin.test(data.summaryEn) ||
      /<(script|iframe|object|embed|form|style)\b|\bon[a-z]+\s*=|javascript:/i.test(body))
    throw new Error('Invalid bilingual metadata or markup in ' + name);
  if (collection === 'daily' ? data.category !== 'briefing' ||
      new Intl.DateTimeFormat('sv-SE', { timeZone: 'Asia/Shanghai', year: 'numeric', month: '2-digit', day: '2-digit' })
        .format(new Date(data.published)) !== slug.replace(/^weekly-/, '') : data.category === 'briefing')
    throw new Error('Invalid article date or category in ' + name);
  return { ...data, collection, slug };
});

export const articles = ['news', 'daily'].flatMap((kind) => read('src/content/' + kind, kind));
const used = new Set();
const titles = new Set();
const projects = new Set();
for (const story of articles) {
  if (story.project) {
    if (projects.has(story.project)) throw new Error('Duplicate project profile ' + story.project);
    projects.add(story.project);
  }
  const title = story.titleEn.toLowerCase().trim();
  if (titles.has(title)) throw new Error('Duplicate article title ' + title);
  titles.add(title);
  for (const source of story.sources) {
    const url = new URL(source.url);
    url.hash = '';
    url.pathname = url.pathname.replace(/\/$/, '') || '/';
    for (const key of [...url.searchParams.keys()]) {
      if (/^(utm_|fbclid$|gclid$)/i.test(key)) url.searchParams.delete(key);
    }
    url.searchParams.sort();
    if (story.collection === 'news' && (!story.type || source === story.sources[0])) {
      if (used.has(url.href)) throw new Error('Duplicate primary article source ' + url.href);
      used.add(url.href);
    }
  }
}
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  console.log(JSON.stringify(articles));
}
