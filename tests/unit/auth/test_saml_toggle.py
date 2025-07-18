import os
from powerdnsadmin.lib.auth import get_saml_class


def test_get_saml_class_modern(monkeypatch):
    monkeypatch.setenv('SAML_IMPLEMENTATION', 'modern')
    from powerdnsadmin.lib.auth.saml_modern import SAML as Modern
    assert get_saml_class() is Modern


def test_get_saml_class_legacy(monkeypatch):
    monkeypatch.delenv('SAML_IMPLEMENTATION', raising=False)
    from powerdnsadmin.lib.auth.saml_legacy import SAML as Legacy
    assert get_saml_class() is Legacy
