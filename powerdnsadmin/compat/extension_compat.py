"""Wrappers for Flask extension compatibility."""

from __future__ import annotations

try:
    from flask_mail import Mail
except Exception:  # pragma: no cover
    Mail = object  # type: ignore


__all__ = ["Mail"]
