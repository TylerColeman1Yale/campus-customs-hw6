# HW 6 — Campus Customs Vendor Desk

## Setup

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
cp .env.example ../.env
# Put the Portkey key in ../.env as PORTKEY_API_KEY=...
```

Run one document from this folder:

```bash
.venv/bin/python agent.py --doc data/practice_docs/p01_bluehen_quote.html
```

Use `--no-defenses` only for the attack tests. It still cannot send email or approve payments: those functions append only to `output/trap_calls.json`.

## Files

`agent.py` is the CLI and PydanticAI agent; `tools.py` reads HTML, PDF, and email documents and defines the log-only traps; `models.py` defines the structured result. Measured runs and reports are under `output/`. The only model configured is `gpt-6-luna` through Portkey.
