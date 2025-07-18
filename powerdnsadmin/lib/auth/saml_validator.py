import os
import logging
from saml2.sigver import CertificateError


logger = logging.getLogger("saml_validator")

REQUIRED_KEYS = [
    "SAML_METADATA_URL",
    "SAML_SP_ENTITY_ID",
]


def validate(app_config):
    missing = [k for k in REQUIRED_KEYS if not app_config.get(k)]
    if missing:
        raise ValueError(f"Missing SAML configuration: {missing}")

    cert = app_config.get("SAML_CERT")
    key = app_config.get("SAML_KEY")
    if cert and not os.path.exists(cert):
        raise CertificateError(f"Certificate file {cert} not found")
    if key and not os.path.exists(key):
        raise CertificateError(f"Key file {key} not found")
    logger.debug("SAML configuration validated")
    return True
