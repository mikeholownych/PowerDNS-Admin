"""Utility helpers for migrating legacy SAML settings."""

from flask import current_app

LEGACY_FLAG = 'legacy'
MODERN_FLAG = 'modern'


def migrate_config(setting_model):
    """Ensure new configuration keys exist."""
    if setting_model.get('saml_enabled') and not setting_model.get('saml_implementation'):
        setting_model.set('saml_implementation', LEGACY_FLAG)
        current_app.logger.info('SAML migration: defaulting implementation to legacy')
