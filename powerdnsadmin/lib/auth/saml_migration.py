import logging

logger = logging.getLogger("saml_migration")

LEGACY_PREFIX = "SAML_"
MODERN_PREFIX = "SAML_"


def migrate_config(app_config):
    """Migrate legacy SAML configuration to modern format."""
    migrated = {}
    for key, value in app_config.items():
        if key.startswith(LEGACY_PREFIX):
            migrated[key] = value
    logger.info("Migrated %d SAML settings", len(migrated))
    return migrated

