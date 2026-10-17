import asyncio, json
from pathlib import Path
from agent import run_document

ROOT = Path(__file__).parent

async def main():
    old = json.loads((ROOT / 'output' / 'cache_test.json').read_text())
    kept = [row for row in old if row.get('setup') == 'with_cache']
    fresh = []
    for path in sorted((ROOT / 'data' / 'practice_docs').iterdir()):
        fresh.append(await run_document(str(path), True, 'without_cache'))
    (ROOT / 'output' / 'cache_test.json').write_text(json.dumps(kept + fresh, indent=2) + '\n')

asyncio.run(main())
