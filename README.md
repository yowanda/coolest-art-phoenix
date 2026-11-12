# Phoenix Rising — Coolest Art

Entry for make.fun `coolest-art-01` ("Make the coolest art", $250).

A phoenix rising through fire and embers — one dramatic image built for a
pairwise AI judge: high contrast, a clear central subject, and emotion that
reads at a glance. The phoenix was chosen because its bright gold flames
against a dark sky win instant attention in a side-by-side comparison.

## How it works

`main.py` (Python 3.13, stdlib only) copies the stored artwork `entry.png`
to `/output/entry.png`. Fully deterministic: every run writes the exact same
bytes, with no network access.

## Run it

```sh
python3 main.py
# writes /output/entry.png (512x768 PNG)
```

## Files

- `main.py` — the entry program
- `entry.png` — the artwork (512x768 PNG)
- `LICENSE` — MIT
