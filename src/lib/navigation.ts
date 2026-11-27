import categories from '../../config/technology-categories.json';
import types from '../../config/content-types.json';

export { categories, types };
export type TechnologyCategory = keyof typeof categories;
type Label = readonly [string, string];

const link = (href: string, zh: string, en: string) => ({ href, label: [zh, en] as const });

export const sections = {
  home: link('/', '首页', 'Home'),
  news: link('/news/', '资讯', 'News'),
  discover: link('/discover/', '发现', 'Discover'),
  learn: link('/learn/', '实践', 'Learn'),
  stories: link('/stories/', '故事', 'Stories'),
  daily: link('/daily/', '每日简报', 'Daily'),
  weekly: link('/weekly/', '每周精选', 'Weekly'),
};

export const hubs = {
  discover: sections.discover.label,
  learn: sections.learn.label,
  stories: sections.stories.label,
};

export const technologyLink = (key: TechnologyCategory) =>
  link(`/category/${key}/`, categories[key][0], categories[key][1]);
export const technologyLinks = (Object.keys(categories) as TechnologyCategory[])
  .filter((key) => key !== 'briefing').map(technologyLink);

export const topicLink = (key: keyof typeof types) =>
  link(`/topics/${key}/`, types[key][0], types[key][1]);
export const topicSection = (key: keyof typeof types) => sections[types[key][2] as keyof typeof sections];

export const technologyIndex = link('/entities/', '全部技术主题', 'All technology topics');
export const rss = link('/rss.xml', 'RSS', 'RSS');

export const footerGroups = [
  { label: ['内容', 'Content'], links: [
    link(sections.news.href, '最新资讯', 'Latest news'), sections.learn, sections.stories, sections.daily, sections.weekly,
  ] },
  { label: ['探索', 'Explore'], links: [
    technologyLink('models'), technologyLink('coding'), technologyLink('agents'), technologyLink('open-source'),
    link(sections.discover.href, '资源目录', 'Resource directory'), technologyIndex,
  ] },
  { label: ['网站', 'Site'], links: [
    link('/about/', '关于我们', 'About'), link('/editorial/', '编辑政策', 'Editorial policy'),
    link('/stats/', '内容统计', 'Publishing stats'), link('/archive/', '文章归档', 'Archive'),
    link('/tags/', '标签索引', 'Tag index'),
  ] },
  { label: ['连接', 'Connect'], links: [
    rss, link('https://github.com/yabby-groups/codex-venture', 'GitHub', 'GitHub'),
    link('/contact/', '联系我们', 'Contact'),
  ] },
] satisfies { label: Label; links: ReturnType<typeof link>[] }[];

export const legalLinks = [
  link('/privacy/', '隐私政策', 'Privacy policy'), link('/terms/', '使用条款', 'Terms of use'),
  link('/affiliate-disclosure/', '联盟推广披露', 'Affiliate disclosure'),
];
