"""Compatibility helpers for utilities removed from ``distutils``.

This module exposes :data:`strtobool` and :data:`StrictVersion` regardless of
Python version.  ``distutils`` was deprecated in Python 3.10 and removed in
3.12.  The helpers below attempt to import these utilities from the standard
library first and fall back to :mod:`setuptools` or :mod:`packaging` when
necessary.
"""

from __future__ import annotations

try:  # Python < 3.12
    from distutils.util import strtobool
    from distutils.version import StrictVersion  # type: ignore
except ModuleNotFoundError:  # Python >= 3.12
    try:
        from setuptools._distutils.util import strtobool  # type: ignore
        from setuptools._distutils.version import StrictVersion  # type: ignore
    except Exception:  # pragma: no cover - last resort
        from packaging.version import Version as StrictVersion  # type: ignore

        def strtobool(val: str) -> int:
            """Return ``1`` for truthy strings and ``0`` for falsey strings."""
            val = val.lower()
            if val in ("y", "yes", "t", "true", "on", "1"):
                return 1
            if val in ("n", "no", "f", "false", "off", "0"):
                return 0
            raise ValueError(f"invalid truth value {val!r}")

__all__ = ["strtobool", "StrictVersion"]
