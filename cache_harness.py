import asyncio, json
from pathlib import Path
from agent import run_document

ROOT = Path(__file__).parent

async def main():
    rows = []
    for setup in ('with_cache', 'without_cache'):
        for path in sorted((ROOT / 'data' / 'practice_docs').iterdir()):
            row = await run_document(str(path), True, setup)
            rows.append(row)
    (ROOT / 'output' / 'cache_test.json').write_text(json.dumps(rows, indent=2) + '\n')

asyncio.run(main())
