# HW 6 run harness

`harness.py` runs every file in `data/practice_docs/` once with defenses enabled and once with `--no-defenses`, compares each structured result with `data/practice_key.json`, and writes the comparison JSON files. The final defended practice rerun also applies the code-level policy validation and is recorded in `defense_results.json`.

Exam documents were run separately by the final defended agent and recorded without consulting an answer key.
