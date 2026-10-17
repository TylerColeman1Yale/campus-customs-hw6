# Problem 2 — Handbook size and cost estimate

## Method

I read `data/shop_handbook.md` as UTF-8 and counted its tokens with the `o200k_base` tokenizer from `tiktoken`. This is a tokenizer-based estimate for the handbook text alone; it excludes the vendor document, prompt wrappers, tool messages, and model output. The handbook contains 28,903 characters, 6,127 whitespace-separated words, and 10,058 tokenizer tokens.

## Rates

The rates below come from `data/prices.json` for `gpt-6-luna`:

- Uncached input: $0.10 per 1,000,000 tokens
- Cached input: $0.01 per 1,000,000 tokens
- Output is excluded because this is a handbook-only input estimate.

## Math

For one call:

```text
uncached = 10,058 / 1,000,000 × $0.10 = $0.0010058
cached   = 10,058 / 1,000,000 × $0.01 = $0.00010058
```

For 1,000 calls:

```text
uncached = $0.0010058 × 1,000 = $1.0058
cached   = $0.00010058 × 1,000 = $0.10058
```

These are estimates for comparison with the API-reported token counts and measured costs in later problems. Actual calls also contain document/prompt input and generated output.
