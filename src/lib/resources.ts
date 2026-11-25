import { getCollection } from 'astro:content';
import { storyUrl, types, type Story } from './content';
import { repositorySnapshot } from './repositories';
import { resourceTypes, type ResourceType } from './resource-schema';

export const resourcePageSize = 12;
export const resourceBase = (type: ResourceType) => `/topics/${type}/`;
export const resourcePage = (type: ResourceType, page: number) =>
  page === 1 ? resourceBase(type) : `${resourceBase(type)}page/${page}/`;

export const directoryCopy: Record<ResourceType, [string, string]> = {
  skills: ['浏览可为 Agent 增加具体能力的技能，按平台和任务查找。', 'Find skills that give agents specific capabilities, by platform and task.'],
  plugins: ['查找扩展应用功能的插件及官方安装入口。', 'Find application extensions and their official installation listings.'],
  mcp: ['按能力查找 MCP 服务器，核对传输方式、部署及权限。', 'Find MCP servers by capability and check their transport, deployment and permissions.'],
  tools: ['按任务查找工具、运行方式和官方资料。', 'Browse tools by task, how they run and where to learn more.'],
  models: ['查找模型权重、模态与发布资料。', 'Find model weights, modalities and release documentation.'],
  'open-source': ['探索有公开代码和官方仓库的项目。', 'Explore projects with public code and official repositories.'],
  prompts: ['按任务查找可复用的提示词与预期输出。', 'Find reusable prompts and expected outputs by task.'],
  workflows: ['浏览可复用的工作流、工具组合和操作步骤。', 'Explore reusable workflows, tool combinations and practical steps.'],
  resources: ['查找参考文档与可复用的实践资料。', 'Find reference documentation and reusable practical resources.'],
};

export const directoryTitle = (type: ResourceType) => type === 'skills' ? ['AI 技能库', 'Agent Skills'] : types[type];

const profiles = (await getCollection('resources')).map(({ id, data }) => {
  if (id !== data.id) throw new Error(`Resource filename differs from ID: ${id}`);
  return data;
});

export function resourceCatalog(stories: Story[]) {
  const related = Map.groupBy(stories.flatMap((story) =>
    (story.data.resourceIds ?? []).map((id) => ({ id, story }))), ({ id }) => id);
  const ids = new Set(profiles.map(({ id }) => id));
  const routes = new Set(stories.map(storyUrl));
  for (const id of related.keys()) {
    if (!ids.has(id)) throw new Error(`Unknown resource relation: ${id}`);
  }
  const resources = profiles.map((resource) => {
    const matches = (related.get(resource.id) ?? []).map(({ story }) => story);
    const github = resource.type === 'open-source' ? repositorySnapshot(resource.repository) : undefined;
    if (resource.detail && !routes.has(resource.detail)) throw new Error(`Unknown resource detail: ${resource.id}`);
    return {
      ...resource, github,
      license: resource.license ?? (github?.license === 'NOASSERTION' ? undefined : github?.license ?? undefined),
      detail: resource.detail ?? resource.site, verified: resource.verifiedAt, added: resource.addedAt,
      tags: [...new Set([...resource.tags, ...matches.flatMap((story) => story.data.tags)])],
      articles: [...new Set(matches.map(storyUrl))],
    };
  });
  const identities = new Set<string>();
  for (const row of resources) {
    const url = new URL(row.site);
    url.hash = '';
    const identity = row.type + ':' + url.href.replace(/\/$/, '');
    if (identities.has(identity)) throw new Error(`Duplicate resource source: ${row.id}`);
    identities.add(identity);
  }
  return resources.sort((a, b) => b.added.localeCompare(a.added) || a.id.localeCompare(b.id));
}

export type Resource = ReturnType<typeof resourceCatalog>[number];
export const resourceDirectories = (stories: Story[]) => {
  const resources = Map.groupBy(resourceCatalog(stories), (resource) => resource.type);
  return resourceTypes.flatMap((type) => {
    const rows = resources.get(type);
    return rows?.length ? [{ type, rows }] : [];
  });
};
