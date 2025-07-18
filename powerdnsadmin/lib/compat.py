"""Compatibility helpers for modules removed in Python 3.12."""

try:  # Python < 3.12
    from distutils.util import strtobool
    from distutils.version import StrictVersion  # type: ignore
except ModuleNotFoundError:  # Python >= 3.12
    from setuptools._distutils.util import strtobool
    from setuptools._distutils.version import StrictVersion

__all__ = ["strtobool", "StrictVersion"]
