"""Read the published resource catalogue for trusted editorial validation."""
import json
from pathlib import Path

DIRECTORY = Path('src/content/resources')


def resource_context():
    return [json.loads(path.read_text()) for path in sorted(DIRECTORY.glob('*.json'))]
