import { unified } from '@astrojs/markdown-remark';
import { defineConfig } from 'astro/config';
import { remarkArticleAnchors } from './src/lib/article-headings.mjs';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  markdown: { processor: unified({ remarkPlugins: [remarkArticleAnchors] }) },
  site: 'https://codex-venture.com',
  trailingSlash: 'always',
  integrations: [sitemap({ filter: (url) => !url.endsWith('/search/') })],
});
