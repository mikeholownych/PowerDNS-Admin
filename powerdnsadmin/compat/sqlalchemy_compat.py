"""Compatibility helpers between SQLAlchemy 1.4 and 2.0."""
from __future__ import annotations

from sqlalchemy import __version__ as sa_version


def is_sa2() -> bool:
    return sa_version.startswith("2")
