import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const schema = z.object({
  titleZh: z.string().min(1),
  titleEn: z.string().min(1),
  summaryZh: z.string().min(1),
  summaryEn: z.string().min(1),
  published: z.iso.datetime({ offset: true }).transform((value) => new Date(value)),
  category: z.enum(['models', 'coding', 'image', 'video', 'audio', 'agents', 'open-source', 'briefing']),
  tags: z.array(z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/)).min(1),
  sources: z.array(z.object({
    title: z.string().min(1),
    url: z.url({ protocol: /^https$/ }),
  })).min(1),
});
export const collections = {
  news: defineCollection({ loader: glob({ pattern: '*.md', base: './src/content/news' }), schema }),
  daily: defineCollection({ loader: glob({ pattern: '*.md', base: './src/content/daily' }), schema }),
};
