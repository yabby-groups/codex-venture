import { spawn } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { setTimeout } from 'node:timers/promises';
import { chromium } from 'playwright';

const routes = process.argv[2]
  ? JSON.parse(await readFile(process.argv[2], 'utf8'))
  : ['news/venture-evidence-publication-workflow/', 'news/ollama-macos-local-check/', 'news/ollama-lm-studio-local-api/', 'news/ragflow-document-retrieval/', 'news/mcp-filesystem-read-only/', 'news/claude-pdf-skill/', 'daily/2026-11-24/'];
if (!routes.length) process.exit(0);
if (routes.some((route) => !/^(news|daily)\/[a-z0-9-]+\/$/.test(route))) throw new Error('Invalid article route');

const origin = 'http://127.0.0.1:4382';
const server = spawn('python3', ['-m', 'http.server', '4382', '--bind', '127.0.0.1', '--directory', 'dist'], { stdio: 'ignore' });
let browser;
try {
  for (let attempt = 0; attempt < 40; attempt++) {
    if (server.exitCode !== null) throw new Error('Preview server exited');
    if (await fetch(origin).then((response) => response.ok).catch(() => false)) break;
    if (attempt === 39) throw new Error('Preview server did not start');
    await setTimeout(200);
  }
  browser = await chromium.launch(process.env.VENTURE_CHROME ? { executablePath: process.env.VENTURE_CHROME } : {});
  const page = await browser.newPage({ userAgent: 'Codex-Venture-Test/1.0' });
  await page.route('**/*', (route) => new URL(route.request().url()).origin === new URL(origin).origin
    ? route.continue() : route.abort());
  for (const route of routes) {
    for (const [width, colorScheme] of [[1440, 'light'], [360, 'dark']]) {
      await page.setViewportSize({ width, height: 900 });
      await page.emulateMedia({ colorScheme });
      const response = await page.goto(origin + '/' + route);
      if (!response?.ok()) throw new Error(`Missing article ${route}`);
      const issues = await page.evaluate(async () => {
        const issues = [];
        const article = document.querySelector('.editorial-article');
        if (!article) return ['article missing'];
        if (!article.querySelector('h1 > [lang="zh-CN"]') || !article.querySelector('h1 > [lang="en"]')) issues.push('bilingual title missing');
        if (document.documentElement.scrollWidth > innerWidth) issues.push('page overflows viewport');
        if (!article.querySelector('.prose p[lang="en"]')) issues.push('bilingual prose missing');
        for (const link of article.querySelectorAll('.article-toc a')) {
          if (!document.getElementById(link.hash.slice(1))) issues.push(`missing anchor ${link.hash}`);
        }
        for (const image of article.querySelectorAll('figure img')) {
          image.loading = "eager";
          await image.decode().catch(() => issues.push(`cannot decode ${image.src}`));
          if (image.naturalWidth !== Number(image.getAttribute('width')) || image.naturalHeight !== Number(image.getAttribute('height'))) issues.push(`dimension mismatch ${image.src}`);
        }
        for (const block of article.querySelectorAll('.article-code')) {
          const pre = block.querySelector('pre');
          if (!pre?.querySelector('code')?.textContent.trim() || block.querySelector('[data-copy]').hidden) {
            issues.push('code or copy control missing');
            continue;
          }
          const colors = getComputedStyle(pre);
          const expectedDark = colors.getPropertyValue('--shiki-dark-bg').trim();
          if (matchMedia('(prefers-color-scheme: dark)').matches && expectedDark &&
            colors.backgroundColor === 'rgb(255, 255, 255)') issues.push('code uses a light background in dark mode');
        }
        return issues;
      });
      if (issues.length) throw new Error(`${route} ${width} ${colorScheme}: ${issues.join(', ')}`);
    }
  }
  console.log(`Checked ${routes.length} article routes in Chromium at desktop and mobile widths`);
} finally {
  await browser?.close();
  server.kill();
}
