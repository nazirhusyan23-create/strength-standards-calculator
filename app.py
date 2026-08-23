# -*- coding: utf-8 -*-
"""
Strength Standards Calculator Collection — Flask backend.

Run:
    pip install -r requirements.txt
    flask --app app run --debug

Then open http://127.0.0.1:5000/
"""
from datetime import date

from flask import Flask, render_template, request, jsonify, abort, Response, url_for

from data import CALCULATORS, ORDER, TIER_ORDER
from icons import icon_for

app = Flask(__name__)

LB_PER_KG = 2.20462

ADSENSE_PUBLISHER_ID = "pub-2006445566626425"
CONTACT_EMAIL = "nh6639741@gmail.com"


# --------------------------------------------------------------------
# Core math (shared by every calculator type)
# --------------------------------------------------------------------
def epley_1rm(weight, reps):
    """Epley formula, reps capped at 12 for accuracy."""
    reps = max(1, min(reps, 12))
    return weight * (1 + reps / 30)


def find_tier(value, tiers):
    """
    tiers: {"Beginner": [lo, hi], ...} in TIER_ORDER.
    Returns dict with tier name, progress % within tier, and how much
    more (in the same unit as `value`) is needed to reach the next tier.
    """
    for i, name in enumerate(TIER_ORDER):
        lo, hi = tiers[name]
        if value < hi or name == "Elite":
            if hi == float("inf"):
                progress = 100.0
                next_tier = None
                remaining = 0.0
            else:
                span = hi - lo
                progress = 0.0 if span <= 0 else max(0.0, min(100.0, (value - lo) / span * 100))
                next_tier = TIER_ORDER[i + 1] if i + 1 < len(TIER_ORDER) else None
                remaining = max(0.0, hi - value)
            return {
                "tier": name,
                "progress_pct": round(progress, 1),
                "next_tier": next_tier,
                "remaining_to_next": round(remaining, 3),
                "tier_index": i,
                "total_tiers": len(TIER_ORDER),
            }
    # value is at/above the top bound of Elite's lower edge already handled above
    last = TIER_ORDER[-1]
    return {
        "tier": last,
        "progress_pct": 100.0,
        "next_tier": None,
        "remaining_to_next": 0.0,
        "tier_index": len(TIER_ORDER) - 1,
        "total_tiers": len(TIER_ORDER),
    }


def to_lb(value, unit):
    return value if unit == "lb" else value * LB_PER_KG


# --------------------------------------------------------------------
# Routes — pages
# --------------------------------------------------------------------
@app.route("/")
def hub():
    cards = [{"slug": s, "icon": icon_for(CALCULATORS[s]["category"]), **CALCULATORS[s]} for s in ORDER]
    return render_template("hub.html", cards=cards)


def _fmt_bound(v, input_type):
    if v == float("inf"):
        return None  # open-ended, template shows "+"
    if input_type in ("reps_weighted", "ratio_external"):
        return f"{v:g}x"
    if input_type == "reps_only":
        return f"{int(v)}"
    if input_type == "time_only":
        return f"{int(v)}s"
    return str(v)


def _rows_for(tiers, input_type):
    rows = []
    for name in TIER_ORDER:
        lo, hi = tiers[name]
        lo_s = _fmt_bound(lo, input_type)
        hi_s = _fmt_bound(hi, input_type)
        if hi_s is None:
            range_str = f"{lo_s}+"
        elif lo == 0:
            range_str = f"< {hi_s}"
        else:
            range_str = f"{lo_s} – {hi_s}"
        rows.append({"tier": name, "range": range_str})
    return rows


def build_table_data(calc):
    input_type = calc["input_type"]
    if calc.get("has_variant_toggle"):
        return {
            sex: {
                variant: _rows_for(calc["tiers"][sex][variant], input_type)
                for variant in ("wall", "freestanding")
            }
            for sex in ("male", "female")
        }
    return {
        sex: _rows_for(calc["tiers"][sex], input_type)
        for sex in ("male", "female")
    }


@app.route("/calculator/<slug>")
def calculator_page(slug):
    calc = CALCULATORS.get(slug)
    if not calc:
        abort(404)
    related = [{"slug": s, "name": CALCULATORS[s]["name"]}
               for s in ORDER if s != slug]
    table_data = build_table_data(calc)
    return render_template(
        "calculator.html",
        slug=slug,
        calc=calc,
        related=related,
        tier_order=TIER_ORDER,
        table_data=table_data,
        icon=icon_for(calc["category"]),
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/privacy-policy")
def privacy():
    return render_template("privacy.html", contact_email=CONTACT_EMAIL,
                            updated_date=date.today().strftime("%B %-d, %Y"))


@app.route("/contact")
def contact():
    return render_template("contact.html", contact_email=CONTACT_EMAIL)


# --------------------------------------------------------------------
# API — computation happens server-side (Python backend)
# --------------------------------------------------------------------
@app.route("/api/calculate/<slug>", methods=["POST"])
def calculate(slug):
    calc = CALCULATORS.get(slug)
    if not calc:
        return jsonify({"error": "unknown calculator"}), 404

    payload = request.get_json(silent=True) or {}
    sex = payload.get("sex", "male")
    if sex not in ("male", "female"):
        sex = "male"
    unit = payload.get("unit", "lb")  # 'lb' or 'kg'

    input_type = calc["input_type"]

    try:
        if input_type == "reps_weighted":
            bodyweight = to_lb(float(payload.get("bodyweight", 0)), unit)
            added = to_lb(float(payload.get("added_weight", 0) or 0), unit)
            reps = int(payload.get("reps", 0))
            if bodyweight <= 0:
                return jsonify({"error": "Enter a valid bodyweight."}), 400
            total_load = bodyweight + added
            one_rm = epley_1rm(total_load, reps)
            ratio = one_rm / bodyweight
            tiers = calc["tiers"][sex]
            result = find_tier(ratio, tiers)
            result.update({
                "one_rm_lb": round(one_rm, 1),
                "one_rm_kg": round(one_rm / LB_PER_KG, 1),
                "ratio": round(ratio, 3),
                "metric": "ratio",
            })

        elif input_type == "ratio_external":
            bodyweight = to_lb(float(payload.get("bodyweight", 0)), unit)
            lifted = to_lb(float(payload.get("weight_lifted", 0)), unit)
            reps = int(payload.get("reps", 0))
            if bodyweight <= 0:
                return jsonify({"error": "Enter a valid bodyweight."}), 400
            one_rm = epley_1rm(lifted, reps)
            ratio = one_rm / bodyweight
            tiers = calc["tiers"][sex]
            result = find_tier(ratio, tiers)
            result.update({
                "one_rm_lb": round(one_rm, 1),
                "one_rm_kg": round(one_rm / LB_PER_KG, 1),
                "ratio": round(ratio, 3),
                "metric": "ratio",
            })

        elif input_type == "reps_only":
            reps = float(payload.get("reps", 0))
            if calc.get("has_variant_toggle"):
                variant = payload.get("variant", "wall")
                if variant not in ("wall", "freestanding"):
                    variant = "wall"
                tiers = calc["tiers"][sex][variant]
            else:
                tiers = calc["tiers"][sex]
            result = find_tier(reps, tiers)
            result.update({"reps": reps, "metric": "reps"})

        elif input_type == "time_only":
            seconds = float(payload.get("seconds", 0))
            tiers = calc["tiers"][sex]
            result = find_tier(seconds, tiers)
            result.update({"seconds": seconds, "metric": "time"})

        else:
            return jsonify({"error": "unsupported calculator type"}), 500

    except (TypeError, ValueError):
        return jsonify({"error": "Please enter valid numbers."}), 400

    result["sex"] = sex
    return jsonify(result)


# --------------------------------------------------------------------
# AdSense / SEO — must be served at the domain root, not under /static
# --------------------------------------------------------------------
@app.route("/ads.txt")
def ads_txt():
    content = f"google.com, {ADSENSE_PUBLISHER_ID}, DIRECT, f08c47fec0942fa0\n"
    return Response(content, mimetype="text/plain")


@app.route("/robots.txt")
def robots_txt():
    sitemap_url = request.url_root.rstrip("/") + "/sitemap.xml"
    content = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {sitemap_url}\n"
    )
    return Response(content, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    today = date.today().isoformat()
    urls = [{"loc": url_for("hub", _external=True), "priority": "1.0"}]
    urls += [
        {
            "loc": url_for("calculator_page", slug=s, _external=True),
            "priority": "0.8",
        }
        for s in ORDER
    ]
    urls += [
        {"loc": url_for("about", _external=True), "priority": "0.5"},
        {"loc": url_for("privacy", _external=True), "priority": "0.3"},
        {"loc": url_for("contact", _external=True), "priority": "0.5"},
    ]
    xml_parts = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        xml_parts.append(
            "<url>"
            f"<loc>{u['loc']}</loc>"
            f"<lastmod>{today}</lastmod>"
            "<changefreq>monthly</changefreq>"
            f"<priority>{u['priority']}</priority>"
            "</url>"
        )
    xml_parts.append("</urlset>")
    return Response("".join(xml_parts), mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True)
