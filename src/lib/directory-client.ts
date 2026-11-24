interface IndexRow {
  id: string;
  page: number;
  name: string;
  verified: string;
  releasedAt?: string;
  featured: boolean;
  stars?: number;
  facets: Record<string, string[]>;
  text: string;
}

const orders: Record<string, (a: IndexRow, b: IndexRow) => number> = {
  stars: (a, b) => a.stars === undefined ? Number(b.stars !== undefined) : b.stars === undefined ? -1 : b.stars - a.stars,
  verified: (a, b) => b.verified.localeCompare(a.verified),
  name: (a, b) => a.name.localeCompare(b.name, 'en', { sensitivity: 'base' }),
  featured: (a, b) => Number(b.featured) - Number(a.featured),
  release: (a, b) => (b.releasedAt ?? '').localeCompare(a.releasedAt ?? ''),
};

export async function enhanceDirectory(root: HTMLElement) {
  const base = root.dataset.directory!;
  const size = Number(root.dataset.size);
  const initialPage = Number(root.dataset.staticPage);
  const search = root.querySelector<HTMLInputElement>('#q')!;
  const grid = root.querySelector<HTMLElement>('[data-cards]')!;
  const empty = root.querySelector<HTMLElement>('[data-empty]')!;
  const sort = root.querySelector<HTMLSelectElement>('[data-sort]')!;
  const result = root.querySelector<HTMLElement>('[data-result]')!;
  const filters = root.querySelector<HTMLDetailsElement>('.resource-filters')!;
  const clientPages = root.querySelector<HTMLElement>('[data-client-pages]')!;
  const staticPages = root.querySelector<HTMLElement>('[data-static-pages]');
  const previous = clientPages.querySelector<HTMLButtonElement>('[data-page-action="-1"]')!;
  const next = clientPages.querySelector<HTMLButtonElement>('[data-page-action="1"]')!;
  const facets = [...root.querySelectorAll<HTMLSelectElement>('[data-facet]')];
  const platforms = [...root.querySelectorAll<HTMLButtonElement>('[data-platform]')];
  const cache = new Map([...grid.querySelectorAll<HTMLElement>('[data-resource]')].map((card) => [card.dataset.resource!, card]));
  let revision = 0;
  let page = initialPage;
  let platform = '';
  let rows: IndexRow[];
  try {
    const response = await fetch(base + 'index.json');
    if (!response.ok) return;
    rows = await response.json();
  } catch {
    return;
  }

  async function loadCards(sourcePage: number) {
    const response = await fetch(sourcePage === 1 ? base : base + 'page/' + sourcePage + '/');
    if (!response.ok) throw new Error('Cannot load resource cards');
    const doc = new DOMParser().parseFromString(await response.text(), 'text/html');
    doc.querySelectorAll<HTMLElement>('[data-cards] > [data-resource]').forEach((card) => cache.set(card.dataset.resource!, card));
  }

  function restore() {
    const params = new URLSearchParams(location.search);
    search.value = params.get('q') ?? '';
    sort.value = params.get('sort') ?? '';
    const requested = params.get('platform') ?? '';
    platform = platforms.some((button) => button.dataset.platform === requested) ? requested : '';
    facets.forEach((filter) => { filter.value = params.get(filter.dataset.facet!) ?? ''; });
    const pathPage = /\/page\/(\d+)\/$/.exec(location.pathname)?.[1];
    page = Math.max(1, Number.parseInt(params.get('p') ?? pathPage ?? '1', 10) || 1);
  }

  async function update(writeUrl: boolean, push = false) {
    const current = ++revision;
    const terms = search.value.normalize('NFKC').trim().toLowerCase().split(/\s+/).filter(Boolean);
    const matching = rows.filter((row) => terms.every((term) => row.text.includes(term)) &&
      (!platform || row.facets.platform.includes(platform)) &&
      facets.every((filter) => !filter.value || row.facets[filter.dataset.facet!]?.includes(filter.value)));
    if (Object.hasOwn(orders, sort.value)) matching.sort(orders[sort.value]);
    const last = Math.max(1, Math.ceil(matching.length / size));
    page = Math.min(page, last);
    const visible = matching.slice((page - 1) * size, page * size);
    platforms.forEach((button) => button.setAttribute('aria-pressed', String(button.dataset.platform === platform)));
    if (writeUrl) {
      const params = new URLSearchParams();
      if (search.value.trim()) params.set('q', search.value.trim());
      if (platform) params.set('platform', platform);
      if (sort.value) params.set('sort', sort.value);
      facets.forEach((filter) => { if (filter.value) params.set(filter.dataset.facet!, filter.value); });
      const unfiltered = !params.size;
      if (!unfiltered && page > 1) params.set('p', String(page));
      const path = unfiltered && page > 1 ? base + 'page/' + page + '/' : base;
      history[push ? 'pushState' : 'replaceState'](null, '', path + (params.size ? '?' + params : ''));
    }
    try {
      await Promise.all([...new Set(visible.filter((row) => !cache.has(row.id)).map((row) => row.page))].map(loadCards));
      if (current !== revision) return;
      const cards = visible.map((row) => cache.get(row.id));
      if (cards.some((card) => !card)) throw new Error('Incomplete resource page');
      grid.replaceChildren(...cards as HTMLElement[]);
      result.textContent = matching.length + ' 项 / ' + matching.length + ' results';
      empty.hidden = matching.length > 0;
      if (staticPages) staticPages.hidden = true;
      clientPages.hidden = last === 1;
      clientPages.querySelector('[data-page-count]')!.textContent = page + ' / ' + last;
      previous.disabled = page === 1;
      next.disabled = page === last;
    } catch {
      if (current !== revision) return;
      result.textContent = '无法加载结果 / Could not load results';
      if (staticPages) staticPages.hidden = false;
    }
  }

  function resetPage() {
    page = 1;
    void update(true);
  }
  restore();
  root.querySelectorAll<HTMLElement>('[data-enhanced]').forEach((element) => { element.hidden = false; });
  filters.open = matchMedia('(min-width: 761px)').matches;
  search.addEventListener('input', resetPage);
  sort.addEventListener('change', resetPage);
  facets.forEach((filter) => filter.addEventListener('change', resetPage));
  platforms.forEach((button) => button.addEventListener('click', () => {
    platform = button.dataset.platform!;
    resetPage();
  }));
  root.querySelector('[data-clear]')!.addEventListener('click', () => {
    search.value = sort.value = platform = '';
    facets.forEach((filter) => { filter.value = ''; });
    resetPage();
  });
  [previous, next].forEach((button) => button.addEventListener('click', () => {
    page += Number(button.dataset.pageAction);
    void update(true, true);
  }));
  addEventListener('popstate', () => { restore(); void update(false); });
  await update(false);
}
