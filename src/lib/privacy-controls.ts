type Consent = { analytics?: boolean; ads?: boolean };
type TcfData = {
  cmpStatus?: string;
  eventStatus?: string;
  gdprApplies?: boolean;
  purpose?: { consents?: Record<number, boolean> };
  vendor?: { consents?: Record<number, boolean> };
};
type ProviderWindow = Window & {
  dataLayer?: unknown[];
  adsbygoogle?: object[];
  __tcfapi?: (command: string, version: number, callback: (data: TcfData, ok: boolean) => void) => void;
};

export function privacyControls() {
  const control = document.querySelector<HTMLElement>('#privacy-settings');
  const form = control?.querySelector('form');
  if (!control || !form) return;
  const { ga, client, cmp } = control.dataset;
  const key = 'venture-privacy-v1';
  let consent: Consent = {};
  try {
    const saved = localStorage.getItem(key);
    if (saved) {
      const value = JSON.parse(saved);
      if (value && typeof value === 'object') {
        consent = { analytics: value.analytics === true, ads: value.ads === true };
      }
    }
  } catch {}
  for (const input of form.querySelectorAll<HTMLInputElement>('input')) {
    input.checked = consent[input.name as keyof Consent] === true;
  }
  const choice = document.querySelector<HTMLElement>('#analytics-choice');
  const save = (value: Consent) => {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch { return; }
    if (ga && value.analytics !== true) {
      Object.assign(window, { ['ga-disable-' + ga]: true });
      for (const name of document.cookie.split(';').map(cookie => cookie.split('=')[0].trim())) {
        if (name !== '_ga' && name !== '_ga_' + ga.slice(2)) continue;
        document.cookie = name + '=; Max-Age=0; Path=/';
        document.cookie = name + '=; Max-Age=0; Path=/; Domain=' + location.hostname;
      }
    }
    location.reload();
  };
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const values = new FormData(form);
    save({ analytics: values.has('analytics'), ads: values.has('ads') });
  });
  form.querySelector('[data-reject]')?.addEventListener('click', () => save({ analytics: false, ads: false }));
  for (const button of choice?.querySelectorAll<HTMLButtonElement>('[data-analytics-choice]') ?? []) {
    button.addEventListener('click', () => save({ ...consent, analytics: button.dataset.analyticsChoice === 'accept' }));
  }

  const nav = navigator as Navigator & { globalPrivacyControl?: boolean };
  if (nav.globalPrivacyControl || nav.doNotTrack === '1') return;
  if (choice && typeof consent.analytics !== 'boolean') choice.hidden = false;
  if (location.origin !== 'https://codex-venture.com' || navigator.webdriver ||
      /HeadlessChrome|Codex-Venture-Test/i.test(navigator.userAgent)) return;
  const providers = window as ProviderWindow;
  const script = (src: string) => {
    const element = document.createElement('script');
    element.src = src;
    element.async = true;
    document.head.append(element);
    return element;
  };
  if (ga && consent.analytics === true) {
    providers.dataLayer ??= [];
    function gtag(..._args: unknown[]) { providers.dataLayer?.push(arguments); }
    gtag('js', new Date());
    gtag('config', ga, { allow_google_signals: false, allow_ad_personalization_signals: false });
    script('https://www.googletagmanager.com/gtag/js?id=' + ga);
  }
  if (!client || !cmp || consent.ads !== true) return;
  let loaded = false;
  script(cmp).addEventListener('load', () => {
    providers.__tcfapi?.('addEventListener', 2, (data, ok) => {
      const allowed = ok && data.cmpStatus === 'loaded' &&
        ['tcloaded', 'useractioncomplete'].includes(data.eventStatus || '') &&
        (data.gdprApplies === false || (data.gdprApplies === true &&
          data.purpose?.consents?.[1] === true && data.vendor?.consents?.[755] === true));
      if (!allowed) {
        if (loaded && ok && data.eventStatus === 'useractioncomplete') location.reload();
        return;
      }
      if (loaded) return;
      const slots = document.querySelectorAll<HTMLTemplateElement>('template[data-venture-ad]');
      if (!slots.length) return;
      loaded = true;
      const ads = providers.adsbygoogle ??= [];
      for (const template of slots) {
        const fragment = template.content.cloneNode(true) as DocumentFragment;
        fragment.querySelector('ins')?.setAttribute('data-ad-client', 'ca-' + client);
        template.replaceWith(fragment);
        ads.push({});
      }
      const tag = script('https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-' + client);
      tag.crossOrigin = 'anonymous';
    });
  });
}
