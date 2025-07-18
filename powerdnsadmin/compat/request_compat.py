"""Request handling helpers to abstract Flask breaking changes."""

from __future__ import annotations

from flask import request


def get_json(silent: bool = False):
    """Return JSON payload in a Flask 2.x/3.x agnostic way."""
    if hasattr(request, "get_json"):
        return request.get_json(silent=silent)
    # Fallback for very old Flask
    try:
        return request.json
    except Exception:  # pragma: no cover
        if silent:
            return None
        raise


__all__ = ["get_json"]
