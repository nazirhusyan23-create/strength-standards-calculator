# -*- coding: utf-8 -*-
"""
Monoline category icons — same visual language as the plate-loading gauge
(bars, plates, straight strokes, no fills). One icon per movement category,
keyed to the `category` field in data.py. Rendered inline (no icon font/
external request) so pages stay fast and self-contained.
"""
from markupsafe import Markup

_WRAP = (
    '<svg viewBox="0 0 28 28" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
    'aria-hidden="true">{}</svg>'
)

_ICONS_RAW = {
    # bar overhead, hands hanging, chevron pulling up toward it
    "Vertical pull": (
        '<line x1="5" y1="7" x2="23" y2="7"/>'
        '<line x1="10" y1="7" x2="10" y2="12"/>'
        '<line x1="18" y1="7" x2="18" y2="12"/>'
        '<path d="M14 23 L14 14 M10.5 17.5 L14 14 L17.5 17.5"/>'
    ),
    # center bar, arrows driving outward left/right
    "Horizontal push": (
        '<line x1="14" y1="5" x2="14" y2="23"/>'
        '<path d="M7 14 L2 14 M4.5 11.2 L2 14 L4.5 16.8"/>'
        '<path d="M21 14 L26 14 M23.5 11.2 L26 14 L23.5 16.8"/>'
    ),
    # barbell (bar + plates) with a press arrow above it
    "Barbell push": (
        '<line x1="5" y1="15" x2="23" y2="15"/>'
        '<rect x="2" y="10" width="4" height="10" rx="1"/>'
        '<rect x="22" y="10" width="4" height="10" rx="1"/>'
        '<path d="M14 10 L14 3 M11 6 L14 3 L17 6"/>'
    ),
    # barbell up top, two straight legs planted under it
    "Barbell lower body": (
        '<line x1="5" y1="7" x2="23" y2="7"/>'
        '<rect x="2" y="3" width="4" height="8" rx="1"/>'
        '<rect x="22" y="3" width="4" height="8" rx="1"/>'
        '<path d="M10 11 L9 24 M18 11 L19 24"/>'
        '<line x1="6.5" y1="24" x2="11.5" y2="24"/>'
        '<line x1="16.5" y1="24" x2="21.5" y2="24"/>'
    ),
    # stance on one bent leg, one leg extended forward
    "Single-leg lower body": (
        '<circle cx="14" cy="6" r="2.2"/>'
        '<line x1="14" y1="8.2" x2="14" y2="16"/>'
        '<path d="M14 16 L8 20"/>'
        '<line x1="5.5" y1="21.5" x2="10.5" y2="18.5"/>'
        '<path d="M14 16 L18 19 L17 24"/>'
    ),
    # stopwatch — reps aren't the metric, time under tension is
    "Isometric hold": (
        '<line x1="11" y1="2.5" x2="17" y2="2.5"/>'
        '<line x1="14" y1="2.5" x2="14" y2="5.5"/>'
        '<circle cx="14" cy="15" r="9.5"/>'
        '<path d="M14 15 L14 9 M14 15 L18.5 17.3"/>'
    ),
    # inverted figure, arms planted, legs stacked overhead
    "Vertical push": (
        '<circle cx="14" cy="23" r="2.2"/>'
        '<line x1="14" y1="20.8" x2="14" y2="8"/>'
        '<path d="M14 8 L9.5 3 M14 8 L18.5 3"/>'
        '<path d="M14 14.5 L8 18.5 M14 14.5 L20 18.5"/>'
    ),
}

CATEGORY_ICONS = {name: Markup(_WRAP.format(body)) for name, body in _ICONS_RAW.items()}

_DEFAULT_RAW = '<line x1="4" y1="14" x2="24" y2="14"/><rect x="2" y="9" width="4" height="10" rx="1"/><rect x="22" y="9" width="4" height="10" rx="1"/>'
DEFAULT_ICON = Markup(_WRAP.format(_DEFAULT_RAW))


def icon_for(category):
    return CATEGORY_ICONS.get(category, DEFAULT_ICON)
