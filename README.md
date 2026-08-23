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

## Search Console, AdSense & SEO plumbing (added)

- **Google Search Console verification** — the meta tag is baked into
  `templates/base.html` (`<meta name="google-site-verification" ...>`), so
  it's live on every page automatically. Once deployed, just click
  "Verify" in Search Console.
- **`ads.txt`** — served at the domain root via a Flask route
  (`app.py` → `/ads.txt`), not a static file, because AdSense requires it
  at exactly `https://yourdomain.com/ads.txt`. Content:
  `google.com, pub-2006445566626425, DIRECT, f08c47fec0942fa0`
- **AdSense loader script** — added to `<head>` in `base.html`, so it's on
  every page site-wide (required for AdSense account approval/crawling).
- **`robots.txt`** and **`sitemap.xml`** — also served via Flask routes
  (`/robots.txt`, `/sitemap.xml`), auto-generated from `data.ORDER` so
  every calculator page (plus the hub) is listed with no manual upkeep.
  `robots.txt` points crawlers at the sitemap automatically using the
  live request host, so it works the same in dev and production.

### Avoiding the "ads on screens without publisher-content" violation

AdSense rejects pages with thin/no content around the ad — that's the
policy hit in the screenshot you shared. Two things this project already
does to avoid it:

1. Every calculator page has real content above any future ad slot: an
   intro paragraph, the calculator, a full standards table, and a 3-question
   FAQ — never just a bare form.
2. The hub page (`/`) now has an "About" section explaining the
   bodyweight-ratio concept, not just a grid of links.

**No `<ins class="adsbygoogle">` ad units are placed yet** — you don't have
slot IDs to give me. `templates/calculator.html` has a comment block right
after the FAQ (i.e. below substantial content, never above it and never on
the empty pre-calculation state) showing exactly where to drop your ad
unit `<ins>`/`<script>` snippet once AdSense gives you slot IDs. Don't
place ads on the hub grid or the empty "fill in the form" result panel —
that's exactly the "screens without publisher-content" pattern Google
flagged in your screenshot.

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
