import os


def get_saml_class():
    impl = os.getenv('SAML_IMPLEMENTATION', 'legacy').lower()
    if impl == 'modern':
        from .saml_modern import SAML
    else:
        from .saml_legacy import SAML
    return SAML


def load_saml():
    return get_saml_class()()
