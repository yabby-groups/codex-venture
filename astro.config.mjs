import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://codex-venture.com',
  trailingSlash: 'always',
  integrations: [sitemap({ filter: (url) => !url.endsWith('/search/') })],
});
