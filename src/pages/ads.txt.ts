import type { APIRoute } from 'astro';
import { publisher } from '../lib/monetization';

export const GET: APIRoute = () => new Response(publisher
  ? `google.com, ${publisher}, DIRECT, f08c47fec0942fa0\n`
  : '# No authorized advertising sellers are configured.\n',
  { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
