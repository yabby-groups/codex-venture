import { readFileSync } from 'node:fs';
import { parse } from 'yaml';

const text = readFileSync(0, 'utf8');
const marker = /^\uFEFF?---[^\S\r\n]*\r?\n([\s\S]*?)\r?\n(?:---|\.\.\.)[^\S\r\n]*(?:\r?\n|$)/;
const match = marker.exec(text);
try {
  const fields = match ? parse(match[1], { maxAliasCount: 0 }) : null;
  const { name, description } = fields ?? {};
  console.log(JSON.stringify(typeof name === 'string' && typeof description === 'string'
    ? { name: name.trim(), description: description.trim() } : {}));
} catch {
  console.log('{}');
}
