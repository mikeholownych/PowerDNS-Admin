"""Compatibility helpers for Flask 2.x and 3.x."""

from __future__ import annotations

import flask


try:
    from flask import json
except ImportError:  # pragma: no cover - Flask <3.0
    import json  # type: ignore


# Unified json dumps/loads
if hasattr(flask, "json"):
    dumps = flask.json.dumps
    loads = flask.json.loads
else:  # pragma: no cover - Flask <3.0
    dumps = json.dumps
    loads = json.loads


__all__ = ["dumps", "loads"]
