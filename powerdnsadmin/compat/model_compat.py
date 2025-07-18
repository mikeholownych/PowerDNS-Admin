"""Compatibility wrappers for legacy models."""
from __future__ import annotations

from typing import Any
from sqlalchemy.orm import DeclarativeBase


class LegacyModelMixin:
    """Mixin providing ``query`` attribute similar to Flask-SQLAlchemy 1.x."""

    @classmethod
    def query(cls) -> Any:  # type: ignore[override]
        from powerdnsadmin.models.base import db

        return db.session.query(cls)
