import { unified } from '@astrojs/markdown-remark';
import { defineConfig } from 'astro/config';
import { remarkArticleAnchors } from './src/lib/article-headings.mjs';
import sitemap from '@astrojs/sitemap';
import { articles } from './scripts/metadata.mjs';

const articleDates = new Map(articles.map((article) => [
  `/${article.collection}/${article.slug}/`,
  article.updated ?? article.published,
]));

export default defineConfig({
  markdown: { processor: unified({ remarkPlugins: [remarkArticleAnchors] }) },
  site: 'https://codex-venture.com',
  trailingSlash: 'always',
  integrations: [sitemap({
    filter: (url) => !['/search/', '/404/', '/404.html'].includes(new URL(url).pathname),
    serialize: (item) => {
      const lastmod = articleDates.get(new URL(item.url).pathname);
      return lastmod ? { ...item, lastmod } : item;
    },
  })],
});
