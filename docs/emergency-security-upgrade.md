# Emergency Security Upgrade Procedure

This document outlines the procedure for applying critical security
upgrades in production. The deployment script `emergency-security-deployment.sh`
performs the following steps:

1. Create a system snapshot for rollback using `scripts/create_system_snapshot.py`.
2. Validate that all upgraded packages are installed via
   `scripts/validate_security_upgrades.py`.
3. Execute the security test suite in `tests/security`.
4. Install packages from `requirements-security-emergency.txt`.
5. Validate that all CVEs are resolved with `scripts/validate_cve_fixes.py`.
6. Run smoke tests to confirm basic functionality.

If any step fails, operators should investigate and, if necessary,
restore from the generated `system-snapshot.json` file.
