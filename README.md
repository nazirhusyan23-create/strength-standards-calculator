# Strength Standards Calculator Collection

Flask backend + server-rendered pages for 15 strength-standards calculators
(6 barbell lifts, 9 bodyweight/calisthenics moves), all driven by one config
file so the design and behavior stay consistent site-wide.

## Run it

```bash
cd strength-calc
pip install -r requirements.txt
flask --app app run --debug
```

Open http://127.0.0.1:5000/ — the hub page links to all 15 calculators.

## How it's built

- **`data.py`** — single source of truth: name, category, input type,
  tier thresholds (male/female), intro copy, and FAQ for all 15 exercises.
  Add calculator #16 by adding one dict entry here.
- **`app.py`** — Flask routes:
  - `/` — hub page (all 15 cards)
  - `/calculator/<slug>` — one page per calculator, rendered from `data.py`
  - `/api/calculate/<slug>` (POST) — **all math runs server-side in Python**
    (Epley 1RM formula, ratio-to-bodyweight, tier lookup, progress-to-next-tier).
    The page just POSTs form values as JSON and renders whatever comes back.
- **`templates/`** — `base.html` (shared shell + disclaimer footer),
  `hub.html`, `calculator.html` (one template renders all 15 pages).
- **`static/css/style.css`** — dark "iron + chalk" theme with a single
  barbell-red accent; signature element is the plate-loading gauge (5
  segments = 5 tiers) instead of a generic progress bar.
- **`static/js/calculator.js`** — reads the form, POSTs to the API, renders
  the tier/gauge/stats, and handles the male/female standards-table toggle.

## Calculator types (from the brief)

| type | inputs | used by |
|---|---|---|
| `reps_weighted` | bodyweight + optional added weight + reps | pull-up, chin-up, dip, ring dip, weighted pull-up |
| `ratio_external` | bodyweight + weight lifted + reps | bench press, squat, deadlift, overhead press, Bulgarian split squat |
| `reps_only` | bodyweight (display) + reps (+ wall/freestanding toggle for HSPU) | push-up, muscle-up, pistol squat, handstand push-up |
| `time_only` | hold time in seconds | L-sit |

Formula (site-wide, per the brief): `1RM = weight × (1 + reps/30)` (Epley),
reps capped at 12 for accuracy.

## ⚠️ Before you publish — verify the tier numbers

Per the brief's own instructions, the thresholds in `data.py` are
**reasonable estimates, not authoritative data**. I ballpark-checked a
couple (pull-up, general bench/squat/deadlift ranges) against published
strength-standards sites and they're in the right neighborhood, but I did
**not** individually verify all 15 exercises × 2 sexes × 5 tiers against
2-3 real sources the way the brief asks. Numbers to double-check hardest
before shipping, since I extrapolated them rather than sourcing them
directly:

- Female thresholds for pull-up, chin-up, dip, ring dip, weighted pull-up
  (I applied the brief's "~60%" / "~55-60%" of male, not sourced directly).
- Handstand push-up female tiers (brief gives no ratio — I estimated).
- Pistol squat and muscle-up exact rep boundaries (brief gives ranges like
  "2-5", I picked single cut points).

## What's not built yet

- No persistence/analytics — it's stateless, one calculation per request.
- No automated tests beyond the manual smoke test used during build
  (all 15 pages load, sample API calls for each of the 4 input types,
  one error case, one 404 case — all passed).
- No deployment config (Procfile/Docker) — add one for your host of choice
  (Render, Railway, Fly.io, a VPS behind gunicorn, etc.) when ready.
