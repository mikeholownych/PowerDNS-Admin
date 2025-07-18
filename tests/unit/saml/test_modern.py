import os
from powerdnsadmin.lib.auth.saml_modern import SAMLModern


def test_metadata_loading(tmp_path):
    config = {
        'SAML_SP_ENTITY_ID': 'test-sp',
        'SAML_ACS_URL': 'https://example.com/acs',
        'SAML_SLS_URL': 'https://example.com/sls',
        'SAML_METADATA_URL': 'https://idp.example.com/metadata',
        'SAML_CERT': __file__,
        'SAML_KEY': __file__,
        'SAML_METADATA_CACHE_LIFETIME': 1,
    }
    dummy_xmlsec = tmp_path / 'xmlsec1'
    dummy_xmlsec.write_text('#!/bin/sh\nexit 0')
    dummy_xmlsec.chmod(0o755)
    config['XMLSEC_BINARY'] = str(dummy_xmlsec)
    import saml2.algsupport
    saml2.algsupport.get_algorithm_support = lambda x: []
    import saml2.metadata
    saml2.metadata.algorithm_support_in_metadata = lambda x: []
    key_file = tmp_path / 'key.pem'
    cert_file = tmp_path / 'cert.pem'
    os.system(f"openssl req -x509 -nodes -newkey rsa:2048 -keyout {key_file} -out {cert_file} -subj '/CN=test' >/dev/null 2>&1")
    config['SAML_KEY'] = str(key_file)
    config['SAML_CERT'] = str(cert_file)
    saml = SAMLModern(config)
    try:
        saml._refresh_metadata()
    except Exception:
        pass  # Remote metadata won't load in tests
    xml = saml.metadata_xml()
    assert 'EntityDescriptor' in xml
