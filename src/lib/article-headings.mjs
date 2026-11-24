const heading = /<h2><span lang="zh-CN">([^<]+)<\/span><span lang="en">([^<]+)<\/span><\/h2>/g;

export function articleHeadings(body) {
  return [...body.matchAll(heading)].map(([, zh, en], index) => ({ id: `section-${index + 1}`, zh, en }));
}

export function remarkArticleAnchors() {
  return (tree) => {
    let index = 0;
    for (const node of tree.children) {
      if (node.type === 'html') {
        node.value = node.value.replace(heading, (markup) => markup.replace('<h2>', `<h2 id="section-${++index}">`));
      }
    }
  };
}
