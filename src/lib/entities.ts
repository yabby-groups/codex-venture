import type { Resource } from './resources';
import type { Story } from './content';

interface Entity {
  id: string;
  name: string;
  type: string;
  aliases: string[];
  site: string;
  repository: string;
  organization: string;
  summary: [string, string];
  guide: [string, string];
  source: string;
  articles: string[];
}

export const entities: Entity[] = [
  {
    id: 'codex-cli', name: 'Codex CLI', type: 'AI coding tool',
    aliases: ['OpenAI Codex CLI'], site: 'https://developers.openai.com/codex/',
    repository: 'https://github.com/openai/codex', organization: 'OpenAI',
    summary: ['Codex CLI 是从终端使用的编程代理，可读取项目、编辑文件和运行命令。', 'Codex CLI is a terminal coding agent that can read projects, edit files and run commands.'],
    guide: ['自动化前先在目标仓库验证工作目录和权限，再分别检查 CLI 退出状态、编辑产物和发布结果。本站的发布记录展示了为什么一次模型调用成功仍需通过独立构建。', 'Before automating, verify the working directory and permissions in the target repository. Check the CLI exit status, editorial output and deployment result separately. Our publication record shows where an independent build fits after a successful model call.'],
    source: 'https://github.com/openai/codex',
    articles: ['codex-cli-0-172-session-navigation', 'codex-playwright-skill', 'agents-md-repository-map', 'venture-evidence-publication-workflow'],
  },
  {
    id: 'mcp', name: 'Model Context Protocol', type: 'Protocol',
    aliases: ['MCP', '模型上下文协议'], site: 'https://modelcontextprotocol.io/',
    repository: 'https://github.com/modelcontextprotocol/modelcontextprotocol', organization: 'Model Context Protocol',
    summary: ['MCP 定义客户端如何发现并调用服务器提供的工具，以及访问资源和提示词。', 'MCP defines how clients discover and call server tools and access resources and prompts.'],
    guide: ['排查连接时，先用 Inspector 区分传输连接、工具发现和具体调用。文件系统服务器应先限定目录，并确认客户端实际暴露的工具和写入权限。', 'When diagnosing a connection, use Inspector to isolate transport, tool discovery and individual calls. For a filesystem server, start with a scoped directory and verify the tools and write permissions actually exposed to the client.'],
    source: 'https://modelcontextprotocol.io/specification/',
    articles: ['mcp-inspector-tool-schema', 'mcp-filesystem-read-only', 'litellm-11103-mcp-registration'],
  },
  {
    id: 'ollama', name: 'Ollama', type: 'Inference engine',
    aliases: [], site: 'https://ollama.com/', repository: 'https://github.com/ollama/ollama',
    organization: 'Ollama',
    summary: ['Ollama 用于下载和运行本地模型，并通过命令行和 HTTP API 提供推理。', 'Ollama downloads and runs local models and exposes inference through a CLI and HTTP API.'],
    guide: ['接入应用前先确认本地服务已启动、模型已安装且 API 能返回结果。对比 LM Studio 时，记录接口路径、模型标识和实际运行环境。', 'Before connecting an application, confirm that the local service is running, the model is installed and the API returns a result. When comparing LM Studio, record the endpoint, model identifier and actual runtime environment.'],
    source: 'https://docs.ollama.com/api/introduction',
    articles: ['ollama-macos-local-check', 'ollama-lm-studio-local-api'],
  },
];

export const entityUrl = (entity: Pick<Entity, 'id'>) => `/entities/${entity.id}/`;
export const entityStories = (entity: Entity, stories: Story[]) =>
  stories.filter((story) => story.collection === 'news' && entity.articles.includes(story.id));
export const storyEntities = (story: Story) =>
  entities.filter((entity) => story.collection === 'news' && entity.articles.includes(story.id));

export function validateEntities(stories: Story[]) {
  const ids = new Set<string>();
  for (const entity of entities) {
    if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(entity.id) || ids.has(entity.id)) {
      throw new Error(`Invalid entity ID: ${entity.id}`);
    }
    ids.add(entity.id);
    if (entity.articles.length < 2 || entityStories(entity, stories).length !== entity.articles.length) {
      throw new Error(`Missing or duplicate article relation: ${entity.id}`);
    }
  }
}

export const entitySchema = (entity: Entity, site: URL | undefined) => ({
  '@type': 'Thing', '@id': new URL(entityUrl(entity) + '#entity', site).href,
  name: entity.name, alternateName: entity.aliases, url: entity.site,
});

export const jsonLd = (value: unknown) => JSON.stringify(value).replaceAll('<', '\\u003c');
export const organization = (site: URL | undefined) => ({
  '@type': 'Organization', '@id': new URL('/#organization', site).href,
  name: 'Codex Venture', url: new URL('/', site).href,
});

export const resourceEntityId = (id: string, site: URL | undefined) =>
  new URL('/entities.json#' + id, site).href;

export const resourceEntitySchema = (row: Resource, site: URL | undefined) => ({
  '@type': ['plugins', 'tools'].includes(row.type) ? 'SoftwareApplication'
    : ['skills', 'mcp', 'open-source'].includes(row.type) ? 'SoftwareSourceCode' : 'Thing',
  '@id': resourceEntityId(row.id, site), name: row.name, alternateName: row.nameZh,
  url: new URL(row.detail, site).href, sameAs: row.site,
  ...(row.repository && { codeRepository: row.repository }),
});
