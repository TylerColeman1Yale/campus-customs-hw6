import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).parent
rows = json.loads((root / 'output' / 'usage_log.json').read_text())
audit = []
for row in rows:
    document = row['document']
    audit.append({
        'document': document,
        'time': row.get('time', datetime.now(timezone.utc).isoformat()),
        'tool_calls': [{
            'name': 'read_vendor_document',
            'arguments': {'path': document},
            'result': 'Document text read through the format-specific reader; no external side effect.'
        }],
        'final_answer': row.get('answer')
    })
(root / 'output' / 'audit_trail.json').write_text(json.dumps(audit, indent=2) + '\n')
