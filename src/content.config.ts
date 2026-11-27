import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

import { articleBlock } from './lib/article-blocks';
import { resourceSchema } from './lib/resource-schema';
import { categories, types, type TechnologyCategory } from './lib/navigation';

const schema = z.object({
  titleZh: z.string().min(1),
  titleEn: z.string().min(1),
  summaryZh: z.string().min(1),
  summaryEn: z.string().min(1),
  published: z.iso.datetime({ offset: true }).transform((value) => new Date(value)),
  category: z.enum(Object.keys(categories) as [TechnologyCategory, ...TechnologyCategory[]]),
  type: z.enum(Object.keys(types) as [keyof typeof types, ...(keyof typeof types)[]]).optional(),
  editorial: z.object({ score: z.number().int().min(0).max(100), tier: z.enum(['standard', 'featured', 'lead']) }).optional(),
  updated: z.iso.date().optional(),
  blocks: z.array(articleBlock).max(8).optional(),
  verified: z.iso.date().optional(),
  version: z.string().min(1).optional(),
  status: z.enum(['current', 'needs-review', 'archived']).optional(),
  tested: z.boolean().optional(),
  resourceIds: z.array(z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/)).optional(),
  project: z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/).optional(),
  tags: z.array(z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/)).min(1),
  sources: z.array(z.object({
    title: z.string().min(1),
    url: z.url({ protocol: /^https$/ }),
  })).min(1),
});
export const collections = {
  resources: defineCollection({
    loader: glob({ pattern: '*.json', base: './src/content/resources', generateId: ({ entry }) => entry.replace(/\.json$/, '') }),
    schema: resourceSchema.extend({
      addedAt: z.iso.date(),
      verifiedAt: z.iso.date(),
      tested: z.boolean(),
      detail: z.string().regex(/^\/news\/[a-z0-9-]+\/$/).optional(),
      tags: z.array(z.string()).default([]),
      repositoryId: z.string().optional(),
      sourcePath: z.string().optional(),
      registryId: z.string().optional(),
      identity: z.string().optional(),
      updatedAt: z.iso.date().optional(),
      firstDiscoveredAt: z.iso.date().optional(),
    }),
  }),
  news: defineCollection({ loader: glob({ pattern: '*.md', base: './src/content/news' }), schema }),
  daily: defineCollection({ loader: glob({ pattern: '*.md', base: './src/content/daily' }), schema }),
};
