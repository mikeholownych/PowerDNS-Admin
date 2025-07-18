"""Compatibility wrapper for loading SAML implementation"""
from ..lib.auth import get_saml_class


class SAML(get_saml_class()):
    pass
