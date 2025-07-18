from flask import current_app
from saml2.client import Saml2Client
from saml2.config import Config as Saml2Config
from saml2 import BINDING_HTTP_REDIRECT, BINDING_HTTP_POST

class SAML:
    """Modern SAML handler based on pysaml2"""
    def __init__(self):
        self.client = None
        if current_app and current_app.config.get('SAML_ENABLED', False):
            metadata_url = current_app.config.get('SAML_METADATA_URL')
            entity_id = current_app.config.get('SAML_SP_ENTITY_ID', 'PowerDNS-Admin')
            acs_url = current_app.config.get('SAML_SP_ACS', '/saml/authorized')
            slo_url = current_app.config.get('SAML_SP_SLS', '/saml/sls')
            cfg = {
                'entityid': entity_id,
                'metadata': {'remote': [{'url': metadata_url}]},
                'service': {
                    'sp': {
                        'endpoints': {
                            'assertion_consumer_service': [(acs_url, BINDING_HTTP_POST)],
                            'single_logout_service': [(slo_url, BINDING_HTTP_REDIRECT)],
                        },
                        'allow_unsolicited': True,
                    }
                },
            }
            saml_cfg = Saml2Config()
            saml_cfg.load(cfg)
            saml_cfg.allow_unknown_attributes = True
            self.client = Saml2Client(config=saml_cfg)

    def prepare_flask_request(self, request):
        return {
            'https': 'on' if request.scheme == 'https' else 'off',
            'http_host': request.host,
            'script_name': request.path,
            'get_data': request.args.copy(),
            'post_data': request.form.copy(),
            'query_string': request.query_string,
        }

    def init_saml_auth(self, req):
        return self.client
