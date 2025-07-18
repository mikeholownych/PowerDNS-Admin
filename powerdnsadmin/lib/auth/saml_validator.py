"""Simple validator for SAML settings"""

REQUIRED_KEYS = ['SAML_METADATA_URL', 'SAML_SP_ENTITY_ID']


def validate(app_config):
    missing = [k for k in REQUIRED_KEYS if not app_config.get(k)]
    return missing
