"""Middleware stack for the Flask 3 application."""

from __future__ import annotations

from flask import Flask


def apply_middleware(app: Flask) -> None:
    """Attach middlewares to the app."""
    # Placeholders for future middleware e.g. security headers
    pass
