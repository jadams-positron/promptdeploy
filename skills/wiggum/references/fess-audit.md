# Final fess audit

Run `fess` at most once against the frozen final candidate when risk warrants it. Do not audit every commit. Keep it read-only. Classify findings under `change-control`; repair only blocking and coupled findings within the two-round budget. Report unrelated findings and stop on expansion. Rerun only affected checks and audit concerns after repair.
