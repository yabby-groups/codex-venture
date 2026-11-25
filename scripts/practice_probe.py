"""Run the locked Pagefind CLI on a synthetic, bilingual site without credentials."""
import json
import os
import platform
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = json.loads((ROOT / 'package-lock.json').read_text())
VERSION = PACKAGE['packages']['node_modules/pagefind']['version']
UPSTREAM = 'https://github.com/cloudcannon/pagefind/releases/tag/v' + VERSION


def run():
    binary = ROOT / 'node_modules/.bin/pagefind'
    with tempfile.TemporaryDirectory(prefix='venture-pagefind-') as directory:
        site = Path(directory)
        for language, text in [('en', 'A sample workflow'), ('zh-CN', '示例工作流')]:
            (site / (language + '.html')).write_text(
                f'<!doctype html><html lang="{language}"><head><title>{text}</title></head>'
                f'<body><main data-pagefind-body><h1>{text}</h1><p>{text}</p></main></body></html>',
                encoding='utf-8',
            )
        receipt = dict(tool='Pagefind', version=VERSION, environment=f'{platform.system()} {platform.machine()}',
                       command='pagefind --site .', status='failed', service_cost_usd=0)
        try:
            result = subprocess.run(
                [str(binary), '--site', '.'], cwd=site, timeout=30, capture_output=True, text=True,
                env={'PATH': str(Path(shutil.which('node') or '/usr/bin/node').resolve().parent) + os.pathsep + os.defpath, 'HOME': directory, 'LANG': 'C.UTF-8', 'NO_COLOR': '1'},
            )
            receipt['exit_code'] = result.returncode
            receipt['output'] = '\n'.join(
                line.strip() for line in result.stdout.splitlines()
                if re.search(r'Running Pagefind|Discovered |[Ll]anguages?:|Indexed [0-9]+|Finished', line)
            )[:650]
            metadata = site / 'pagefind/pagefind-entry.json'
            if result.returncode == 0 and metadata.is_file():
                receipt['languages'] = sorted(json.loads(metadata.read_text())['languages'])
                if receipt['languages'] == ['en', 'zh-cn']:
                    receipt['status'] = 'passed'
            if result.returncode:
                receipt['error'] = 'Pagefind exited unsuccessfully'
        except (OSError, ValueError, KeyError, subprocess.TimeoutExpired) as error:
            receipt['error'] = type(error).__name__
        return receipt


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2))
