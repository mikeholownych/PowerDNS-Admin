"""Utility to migrate SAML configuration."""
import json
from powerdnsadmin.lib.auth.saml_migration import migrate_config
from powerdnsadmin.lib.settings import AppSettings


def main():
    settings = AppSettings()
    migrated = migrate_config(settings.settings())
    print(json.dumps(migrated, indent=2))


if __name__ == '__main__':
    main()
