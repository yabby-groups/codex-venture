import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { resolve, sep } from 'node:path';
import { chromium } from 'playwright';

const origin = 'https://codex-venture.com';
const measurementId = 'G-TESTONLY42';
const dist = resolve('dist');
const home = await readFile(resolve(dist, 'index.html'), 'utf8');
assert(home.includes(`data-ga="${measurementId}"`), 'Build with VENTURE_GA4_ID=G-TESTONLY42');
const browser = await chromium.launch(process.env.VENTURE_CHROME ? { executablePath: process.env.VENTURE_CHROME } : {});
try {
  for (const scenario of ['consent', 'automation', 'GPC', 'DNT']) {
    const context = await browser.newContext({
      serviceWorkers: 'block',
      userAgent: scenario === 'automation' ? 'Codex-Venture-Test/1.0' : 'GA4 fixture browser',
      viewport: { width: 360, height: 800 },
    });
    const requests = [];
    await context.route('**/*', async route => {
      const url = new URL(route.request().url());
      if (url.hostname === 'www.googletagmanager.com') {
        requests.push(url.href);
        return route.fulfill({ contentType: 'application/javascript', body: '' });
      }
      if (url.origin !== origin) return route.abort();
      const file = resolve(dist, '.' + url.pathname + (url.pathname.endsWith('/') ? 'index.html' : ''));
      if (!file.startsWith(dist + sep)) return route.abort();
      try { await route.fulfill({ path: file }); } catch { await route.abort(); }
    });
    await context.addInitScript(mode => {
      if (mode !== 'automation') Object.defineProperty(navigator, 'webdriver', { value: false });
      if (mode === 'GPC') Object.defineProperty(navigator, 'globalPrivacyControl', { value: true });
      if (mode === 'DNT') Object.defineProperty(navigator, 'doNotTrack', { value: '1' });
      if (mode !== 'consent') localStorage.setItem('venture-privacy-v1', '{"analytics":true}');
    }, scenario);
    const page = await context.newPage();
    await page.goto(origin);
    const prompt = page.locator('#analytics-choice');
    const tag = page.locator('script[src^="https://www.googletagmanager.com/"]');
    assert.equal(await tag.count(), 0, scenario);
    if (scenario === 'consent') {
      assert(await prompt.isVisible());
      assert(await page.locator('main h1').isVisible());
      assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
      const reloadAfter = async click => {
        await Promise.all([page.waitForNavigation(), click()]);
      };
      await reloadAfter(() => prompt.locator('[data-analytics-choice="reject"]').click());
      assert.equal(await prompt.isVisible(), false);
      assert.equal(await tag.count(), 0);
      await page.locator('[data-open-privacy]').click();
      const checkbox = page.locator('#privacy-settings [name="analytics"]');
      assert(await checkbox.isVisible());
      await checkbox.check();
      await reloadAfter(() => page.locator('#privacy-settings [type="submit"]').click());
      assert.equal(await tag.count(), 1);
      assert(await page.evaluate(id => window.dataLayer.some(command =>
        command[0] === 'config' && command[1] === id && command[2].allow_google_signals === false), measurementId));
      assert.deepEqual(requests, [`https://www.googletagmanager.com/gtag/js?id=${measurementId}`]);
      await context.addCookies([{ name: '_ga_TESTONLY42', value: 'fixture', domain: 'codex-venture.com', path: '/' }]);
      await page.locator('[data-open-privacy]').click();
      await checkbox.uncheck();
      await reloadAfter(() => page.locator('#privacy-settings [type="submit"]').click());
      assert.equal(await tag.count(), 0);
      assert.equal((await context.cookies()).some(cookie => cookie.name === '_ga_TESTONLY42'), false);
      await page.evaluate(() => localStorage.removeItem('venture-privacy-v1'));
      await page.reload();
      await reloadAfter(() => prompt.locator('[data-analytics-choice="accept"]').click());
      assert.equal(await tag.count(), 1);
      assert.equal(requests.length, 2);
    } else {
      assert.equal(requests.length, 0, scenario);
    }
    await context.close();
  }
  console.log('GA4 consent, withdrawal, GPC, DNT and automation isolation verified');
} finally {
  await browser.close();
}
