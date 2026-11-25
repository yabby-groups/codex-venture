import assert from 'node:assert/strict';
import { readdir } from 'node:fs/promises';
import { chromium } from 'playwright';

const origin = process.argv[2] ?? 'http://127.0.0.1:4383';
const browser = await chromium.launch(process.env.VENTURE_CHROME ? { executablePath: process.env.VENTURE_CHROME } : {});
try {
  const page = await browser.newPage();
  const routes = (await readdir('dist', { recursive: true }))
    .filter((path) => path.endsWith('index.html'))
    .map((path) => '/' + path.slice(0, -'index.html'.length));
  for (const [width, height, colorScheme] of [[1440, 900, 'light'], [1280, 800, 'dark'], [390, 844, 'light'], [360, 800, 'dark']]) {
    await page.setViewportSize({ width, height });
    await page.emulateMedia({ colorScheme });
    for (const route of routes) {
      const response = await page.goto(origin + route, { waitUntil: 'domcontentloaded' });
      assert(response?.ok(), route);
      const issues = await page.evaluate(() => {
        const issues = [];
        const main = document.querySelector('main');
        const headings = main.querySelectorAll('h1');
        if (headings.length !== 1 || !headings[0].textContent.trim()) issues.push('missing or repeated H1');
        if (document.documentElement.scrollWidth > innerWidth) issues.push('horizontal overflow');
        if (!document.querySelector('link[rel="canonical"]')?.href.endsWith(location.pathname)) issues.push('wrong canonical');
        for (const schema of document.querySelectorAll('script[type="application/ld+json"]')) JSON.parse(schema.textContent);
        const listing = main.querySelector('.listing-body');
        if (listing) {
          if ([...listing.querySelectorAll('h2')].some(h => h.textContent.replace(/\s/g, '') === '文章Articles')) issues.push('generic Articles heading');
          const count = main.querySelector('.listing-count').textContent;
          if ((count.match(/\d+/g) ?? []).length !== 1) issues.push('repeated article count');
          for (const heading of listing.querySelectorAll('.story-list > li > h2')) {
            if (!heading.querySelector('[lang="en"]')?.textContent.trim() || !heading.checkVisibility()) issues.push('missing visible bilingual story');
          }
          if (!location.pathname.startsWith('/daily/') && listing.querySelector('.rail')) issues.push('irrelevant date sidebar');
        }
        const article = main.querySelector('.editorial-article');
        if (article && (!article.querySelector('h1 [lang="en"]') || !article.querySelector('.prose [lang="en"]'))) issues.push('missing English article content');
        const title = main.querySelector('.listing-title');
        if (title?.children.length === 2) {
          const [heading, count] = [...title.children].map(el => el.getBoundingClientRect());
          if (heading.right > count.left && heading.bottom > count.top && count.bottom > heading.top) issues.push('overlapping heading and count');
        }
        return issues;
      });
      assert.deepEqual(issues, [], `${route} ${width}×${height} ${colorScheme}: ${issues.join(', ')}`);
    }
  }

  await page.goto(origin + '/news/');
  const first = await page.locator('.story-list li h2 a').first().getAttribute('href');
  await page.locator('.pagination a', { hasText: 'Next' }).click();
  assert.match(page.url(), /\/news\/page\/2\/$/);
  assert.notEqual(await page.locator('.story-list li h2 a').first().getAttribute('href'), first);
  await page.locator('.pagination a', { hasText: 'Previous' }).click();
  assert.equal(new URL(page.url()).pathname, '/news/');

  await page.goto(origin + '/daily/');
  assert.equal(await page.getByRole('heading', { name: /日期归档/ }).count(), 1);
  await page.goto(origin + '/learn/');
  assert(await page.locator('main .section-heading h2').count() > 0);
  await page.goto(origin + '/search/?q=Handy');
  await page.locator('#results h2 a[href*="handy"]').first().waitFor();
  assert.equal(await page.locator('#status [lang="en"]').textContent(), 'results');

  await page.goto(origin + '/topics/skills/');
  const input = page.locator('.resource-search input');
  const total = Number(await page.locator('[data-result-count]').textContent());
  await input.fill('venture-test-no-matching-resource');
  await page.locator('[data-empty]').waitFor();
  assert.equal(await page.locator('[data-result-count]').textContent(), '0');
  assert.equal(await page.locator('[data-cards] > article').count(), 0);
  await page.locator('.resource-filters summary').click();
  await page.locator('[data-clear]').click();
  await page.locator('[data-empty]').waitFor({ state: 'hidden' });
  assert.equal(Number(await page.locator('[data-result-count]').textContent()), total);
  await page.locator('[data-sort]').selectOption('name');
  await page.waitForURL(/sort=name/);
  assert(await page.locator('[data-cards] > article').count() > 0);

  const menu = page.locator('.nav-menu summary');
  await menu.focus();
  await page.keyboard.press('Enter');
  assert.equal(await page.locator('.nav-menu[open]').count(), 1);
  assert.equal(await page.locator('.nav-menu [href="/news/"]').count(), 0);
  await page.keyboard.press('Escape');
  assert.equal(await page.locator('.nav-menu[open]').count(), 0);
  console.log(`Checked ${routes.length} routes at four viewport/theme combinations, pagination, Pagefind, resource filters and keyboard navigation`);
} finally {
  await browser.close();
}
