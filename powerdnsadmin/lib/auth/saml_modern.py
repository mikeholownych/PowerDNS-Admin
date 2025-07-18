import logging
import os
from datetime import datetime, timedelta

from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
from saml2 import client, config
from saml2.metadata import entity_descriptor
from saml2.sigver import CertificateError


class SAMLModern:
    """Modern SAML handler using pysaml2."""

    def __init__(self, app_config):
        self.app_config = app_config
        self.logger = logging.getLogger("saml_modern")
        self.sp_config = self._build_sp_config()
        self.client = client.Saml2Client(config=self.sp_config)
        self._metadata_fetched = None
        self._metadata_timestamp = datetime.min

    def _build_sp_config(self):
        conf = config.SPConfig()
        conf.load({
            "entityid": self.app_config.get("SAML_SP_ENTITY_ID"),
            "service": {
                "sp": {
                    "endpoints": {
                        "assertion_consumer_service": [
                            (
                                self.app_config.get("SAML_ACS_URL"),
                                BINDING_HTTP_POST,
                            )
                        ],
                        "single_logout_service": [
                            (
                                self.app_config.get("SAML_SLS_URL"),
                                BINDING_HTTP_REDIRECT,
                            )
                        ],
                    },
                    "allow_unsolicited": True,
                }
            },
            "key_file": self.app_config.get("SAML_KEY"),
            "cert_file": self.app_config.get("SAML_CERT"),
            "xmlsec_binary": self._xmlsec_binary(),
        })
        return conf

    def _xmlsec_binary(self):
        bin_path = self.app_config.get("XMLSEC_BINARY", "/usr/bin/xmlsec1")
        return bin_path if os.path.exists(bin_path) else None

    def _refresh_metadata(self):
        lifetime = timedelta(minutes=self.app_config.get("SAML_METADATA_CACHE_LIFETIME", 1))
        if self._metadata_fetched and datetime.now() - self._metadata_timestamp < lifetime:
            return
        url = self.app_config.get("SAML_METADATA_URL")
        if not url:
            raise ValueError("SAML_METADATA_URL not configured")
        try:
            self.logger.info("Fetching SAML metadata from %s", url)
            self.client.config.load({"metadata": {"remote": [{"url": url}]}})
            self._metadata_fetched = True
            self._metadata_timestamp = datetime.now()
        except Exception as exc:
            self.logger.error("Failed to fetch metadata: %s", exc)
            raise

    def get_authn_request(self, relay_state=""):
        self._refresh_metadata()
        reqid, info = self.client.prepare_for_authenticate(relay_state=relay_state)
        return reqid, dict(info["headers"])

    def process_response(self, request_data):
        self._refresh_metadata()
        response = self.client.parse_authn_request_response(
            request_data.get("SAMLResponse"),
            BINDING_HTTP_POST,
        )
        return response.ava

    def metadata_xml(self):
        ed = entity_descriptor(self.sp_config)
        return ed.to_string().decode()

    def validate_certificate(self):
        cert = self.app_config.get("SAML_CERT")
        if not cert or not os.path.exists(cert):
            raise CertificateError("Certificate not found")
        self.logger.debug("Using certificate %s", cert)
        return True
