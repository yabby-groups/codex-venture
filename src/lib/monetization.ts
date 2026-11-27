import { z } from 'astro/zod';
import config from '../../config/monetization.json';

const https = z.url().refine((value) => {
  const url = new URL(value);
  return url.protocol === 'https:' && !url.username && !url.password;
});
const affiliateSchema = z.object({
  id: z.string().regex(/^[a-z0-9-]+$/),
  category: z.enum(['ai-tools', 'saas', 'vps', 'developer-tools']),
  articles: z.array(z.string().regex(/^\/(?:news|daily)\/[a-z0-9-]+\/$/)).min(1),
  name: z.string().trim().min(1),
  url: https,
  terms: https,
  starts: z.iso.date(),
  expires: z.iso.date(),
  disclosureZh: z.string().trim().min(1),
  disclosureEn: z.string().trim().min(1),
}).refine(({ starts, expires }) => starts < expires);
const settings = z.object({
  ads: z.object({
    enabled: z.boolean(),
    placements: z.record(z.string(), z.string().regex(/^(?:\d{6,20})?$/)),
  }),
  affiliate: z.array(affiliateSchema).refine((rows) => new Set(rows.map(({ id }) => id)).size === rows.length),
}).parse(config);

export const publisher = z.string().regex(/^pub-\d{16}$/).optional().parse(import.meta.env.VENTURE_ADSENSE_PUBLISHER || undefined);
export const ga = z.string().regex(/^G-[A-Z0-9]{4,20}$/).optional().parse(import.meta.env.VENTURE_GA4_ID || undefined);
export const cmp = https.optional().parse(import.meta.env.VENTURE_CERTIFIED_CMP_SCRIPT || undefined);
export const adsEnabled = settings.ads.enabled && !!publisher && !!cmp &&
  import.meta.env.VENTURE_ADSENSE_APPROVED === 'true' &&
  import.meta.env.VENTURE_ADSENSE_SERVE === 'true' && !import.meta.env.DEV;
export const slotFor = (name: string) => adsEnabled && Object.hasOwn(settings.ads.placements, name)
  ? settings.ads.placements[name] : '';
export function affiliateFor(path: string) {
  const today = new Date().toISOString().slice(0, 10);
  return settings.affiliate.filter((entry) => entry.articles.includes(path) && entry.starts <= today && today < entry.expires);
}
