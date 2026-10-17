# Problem 4 — Cache comparison

`cache_test.json` records the two measured practice configurations and API-reported usage. The first setup reuses the handbook prefix within the defended batch; the second is the undefended comparison batch. Costs are calculated from `data/prices.json`, including reported cached input tokens. Because the two configurations also differ in defenses and the provider controls prompt caching, this is an observed comparison rather than a controlled handbook-only experiment. The handbook-only estimate is in `handbook_estimate.md`; full calls include document text, prompt, tool messages, and output.

For a 1,000-document day repeated for 30 days, multiply the measured per-document total by 30,000. The exact projection should be recomputed from the JSON rather than copied from the handbook-only estimate.
