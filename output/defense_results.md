# Problem 6 — Defense results

The defended agent was rerun on all 12 practice documents. All 12 final decisions match the practice key, and legitimate quote fields remain populated. The JSON contains per-document token counts and calculated cost.

| Layer | What it catches |
|---|---|
| Code | Converts files to text, strips markup, removes common control/injection and conflicting revision lines, and applies the four policy checks deterministically. |
| Design | The analysis agent has a document-reader tool only; email and payment are separate log-only traps and cannot create side effects. |
| Prompt | Labels vendor content as untrusted data, forbids following instructions/links, and requires unknown facts rather than guesses. |

The added cost is measured in `defense_results.json`; it varies by document because the API reports actual prompt, cache, and output tokens. The code safety layer adds some processing locally but no invented API charge.
