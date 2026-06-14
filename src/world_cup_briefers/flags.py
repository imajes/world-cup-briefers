from __future__ import annotations

import html

from markupsafe import Markup


_FLAG_SVGS: dict[str, str] = {
    "haiti": """<svg class="mini-flag" viewBox="0 0 120 72" role="img" aria-label="Flag of Haiti" xmlns="http://www.w3.org/2000/svg">
  <rect width="120" height="36" fill="#00209F"/>
  <rect y="36" width="120" height="36" fill="#D21034"/>
  <rect x="44" y="24" width="32" height="24" rx="1.5" fill="#FFFFFF"/>
  <path d="M60 28l4.5 8h-9l4.5-8z" fill="#1B7F3A"/>
  <rect x="52" y="38" width="16" height="4" fill="#8B5A2B"/>
  <path d="M50 45h20" stroke="#D6A400" stroke-width="2"/>
</svg>""",
    "scotland": """<svg class="mini-flag" viewBox="0 0 120 72" role="img" aria-label="Flag of Scotland" xmlns="http://www.w3.org/2000/svg">
  <rect width="120" height="72" fill="#0065BD"/>
  <polygon points="0,0 14,0 120,60 120,72 106,72 0,12" fill="#FFFFFF"/>
  <polygon points="120,0 106,0 0,60 0,72 14,72 120,12" fill="#FFFFFF"/>
</svg>""",
    "germany": """<svg class="mini-flag" viewBox="0 0 120 72" role="img" aria-label="Flag of Germany" xmlns="http://www.w3.org/2000/svg"><rect width="120" height="24" fill="#000"/><rect y="24" width="120" height="24" fill="#DD0000"/><rect y="48" width="120" height="24" fill="#FFCE00"/></svg>""",
    "japan": """<svg class="mini-flag" viewBox="0 0 120 72" role="img" aria-label="Flag of Japan" xmlns="http://www.w3.org/2000/svg"><rect width="120" height="72" fill="#fff"/><circle cx="60" cy="36" r="21" fill="#BC002D"/></svg>""",
    "netherlands": """<svg class="mini-flag" viewBox="0 0 120 72" role="img" aria-label="Flag of the Netherlands" xmlns="http://www.w3.org/2000/svg"><rect width="120" height="24" fill="#AE1C28"/><rect y="24" width="120" height="24" fill="#fff"/><rect y="48" width="120" height="24" fill="#21468B"/></svg>""",
    "australia": """<svg class="mini-flag" viewBox="0 0 120 72" role="img" aria-label="Flag of Australia" xmlns="http://www.w3.org/2000/svg"><rect width="120" height="72" fill="#00008B"/><rect width="60" height="36" fill="#012169"/><path d="M0 0l60 36M60 0L0 36" stroke="#fff" stroke-width="7"/><path d="M0 0l60 36M60 0L0 36" stroke="#C8102E" stroke-width="3"/><path d="M30 0v36M0 18h60" stroke="#fff" stroke-width="11"/><path d="M30 0v36M0 18h60" stroke="#C8102E" stroke-width="6"/><g fill="#fff"><circle cx="88" cy="18" r="3"/><circle cx="102" cy="31" r="3"/><circle cx="88" cy="50" r="3"/><circle cx="72" cy="38" r="4"/></g></svg>""",
    "turkiye": """<svg class="mini-flag" viewBox="0 0 120 72" role="img" aria-label="Flag of Türkiye" xmlns="http://www.w3.org/2000/svg"><rect width="120" height="72" fill="#E30A17"/><circle cx="48" cy="36" r="18" fill="#fff"/><circle cx="55" cy="36" r="14" fill="#E30A17"/><path d="M76 24l3.6 8.2 8.9.7-6.8 5.8 2.1 8.7-7.6-4.6-7.6 4.6 2.1-8.7-6.8-5.8 8.9-.7z" fill="#fff"/></svg>""",
}

ALIASES = {
    "curaçao": "curacao",
    "curacao": "curacao",
    "türkiye": "turkiye",
    "turkiye": "turkiye",
    "turkey": "turkiye",
    "the netherlands": "netherlands",
    "usa": "united states",
}


def flag_svg(country: str, code: str | None = None) -> Markup:
    """Return a safe inline SVG flag or a neutral placeholder."""
    key = ALIASES.get(_normalize(country), _normalize(country))
    if key in _FLAG_SVGS:
        return Markup(_FLAG_SVGS[key])
    label = html.escape(country)
    initials = html.escape((code or country[:3]).upper())
    return Markup(
        f"""<svg class="mini-flag fallback-flag" viewBox="0 0 120 72" role="img" aria-label="Flag placeholder for {label}" xmlns="http://www.w3.org/2000/svg">
  <rect width="120" height="72" rx="8" fill="#eef3f8"/>
  <rect x="8" y="8" width="104" height="56" rx="6" fill="#fff" stroke="#ccd6e2"/>
  <text x="60" y="42" text-anchor="middle" font-family="system-ui, sans-serif" font-size="19" font-weight="800" fill="#48566a">{initials}</text>
</svg>"""
    )


def _normalize(value: str) -> str:
    return value.strip().casefold().replace("ı", "i")
