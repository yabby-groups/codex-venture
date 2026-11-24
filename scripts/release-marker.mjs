import { createHash } from 'node:crypto';
import { readFileSync, readdirSync, writeFileSync } from 'node:fs';

// Stable across the hosted validation and Cloudflare's independent build.
const hash = createHash('sha256');
for (const directory of ['src/content/news', 'src/content/daily']) {
  for (const file of readdirSync(directory).filter((name) => name.endsWith('.md')).sort()) {
    const path = directory + '/' + file;
    hash.update(path + '\0');
    hash.update(createHash('sha256').update(readFileSync(path)).digest());
  }
}
writeFileSync('dist/release.txt', hash.digest('hex') + '\n');
