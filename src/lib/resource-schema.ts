import { z } from 'astro/zod';

const pair = z.tuple([z.string().min(1), z.string().min(1)]);
export const resourceTypes = ['skills', 'plugins', 'mcp', 'tools', 'models', 'open-source', 'prompts', 'workflows', 'resources'] as const;
const https = z.url({ protocol: /^https$/ }).refine((value) => {
  const url = new URL(value);
  return !url.username && !url.password;
});

export const resourceSchema = z.object({
  id: z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/),
  type: z.enum(resourceTypes),
  name: z.string().min(1).max(120),
  nameZh: z.string().min(1).max(120).optional(),
  summary: pair,
  site: https,
  repository: https.optional(),
  verificationSources: z.array(https).optional(),
  platforms: z.array(z.string().min(1)).default([]),
  categories: z.array(pair).min(1),
  license: z.string().optional(),
  install: z.string().optional(),
  transport: z.string().optional(),
  deployment: z.string().optional(),
  kind: z.string().optional(),
  version: z.string().optional(),
  verifiedAt: z.iso.date().optional(),
  releasedAt: z.iso.date().optional(),
  notes: pair.optional(),
  featured: z.boolean().default(false),
});

export type ResourceType = typeof resourceTypes[number];
