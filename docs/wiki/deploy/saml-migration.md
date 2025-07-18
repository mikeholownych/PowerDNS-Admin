# SAML Migration Guide

This document describes migrating from the legacy `python3-saml` backend to the new `pysaml2` implementation.

1. **Enable feature flag**
   Set environment variable `SAML_IMPLEMENTATION=modern` and restart the application. The legacy code remains available for rollback by setting the variable back to `legacy`.
2. **Run migration script**
   Execute `python scripts/saml_migrate.py` to output your current SAML configuration in the new format. Verify values and update your configuration files accordingly.
3. **Monitoring**
   The application logs `saml_modern` messages. Ensure no authentication errors appear before switching all traffic.
4. **Rollback**
   Simply revert `SAML_IMPLEMENTATION` to `legacy` and restart the service.
