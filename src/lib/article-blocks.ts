import { z } from 'astro/zod';

const pair = z.object({
  zh: z.string().trim().min(1).max(600).regex(/\p{Script=Han}/u),
  en: z.string().trim().min(1).max(1000).regex(/[a-z]{2}/i),
}).strict();

const title = { title: pair };
const items = z.array(pair).min(2).max(8);
const row = z.array(pair).min(2).max(4);
const https = z.url({ protocol: /^https$/ });
const language = z.enum(['json', 'yaml', 'toml', 'bash', 'shell', 'python', 'javascript', 'docker', 'nginx', 'text']);

export const articleBlock = z.discriminatedUnion('kind', [
  z.object({ kind: z.enum(['workflow', 'steps', 'timeline', 'takeaways', 'changes']), ...title, items }).strict(),
  z.object({ kind: z.enum(['facts', 'pros-cons', 'comparison']), ...title, columns: row, rows: z.array(row).min(1).max(12) }).strict(),
  z.object({ kind: z.literal('code'), ...title, language, file: z.string().max(100).optional(), code: z.string().min(1).max(6000) }).strict(),
  z.object({ kind: z.literal('notice'), ...title, text: pair }).strict(),
  z.object({
    kind: z.literal('figure'), ...title, alt: pair, caption: pair,
    assetType: z.enum(['product-screenshot', 'project-screenshot', 'product-image', 'logo', 'diagram', 'chart', 'illustration']),
    src: z.string().regex(/^\/article-media\/[a-z0-9][a-z0-9/_-]*\.(?:avif|webp|png|jpe?g)$/),
    source: https, rights: z.string().trim().min(3).max(300),
    width: z.number().int().min(1).max(4096), height: z.number().int().min(1).max(4096),
    verified: z.iso.date(),
  }).strict(),
]).superRefine((block, ctx) => {
  if ('rows' in block && block.rows.some((cells) => cells.length !== block.columns.length)) {
    ctx.addIssue({ code: 'custom', message: 'Table rows must match the number of columns', path: ['rows'] });
  }
});

export type ArticleBlock = z.infer<typeof articleBlock>;
