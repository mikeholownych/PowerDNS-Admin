try:
    from distutils.util import strtobool
except ModuleNotFoundError:  # Python >=3.12
    from setuptools._distutils.util import strtobool

try:
    from distutils.version import StrictVersion
except ModuleNotFoundError:
    from setuptools._distutils.version import StrictVersion

__all__ = ["strtobool", "StrictVersion"]
