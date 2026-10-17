# Problem 4 — Cache comparison

`cache_test.json` records two defended practice configurations and API-reported usage. `with_cache` uses one stable `openai_prompt_cache_key`; `without_cache` uses a different per-document key and a unique prompt-prefix nonce. Costs are calculated from `data/prices.json`, including reported cached input tokens. The Portkey/provider still reported cached tokens in the second setup even after both controls, so the artifact does not falsely claim a zero-cache run; provider-controlled automatic prefix caching remains a limitation. The handbook-only estimate is in `handbook_estimate.md`; full calls include document text, prompt, tool messages, and output.

For a 1,000-document day repeated for 30 days, multiply the measured per-document total by 30,000. The exact projection should be recomputed from the JSON rather than copied from the handbook-only estimate.
