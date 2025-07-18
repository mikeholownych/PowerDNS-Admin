"""Validate that the emergency security upgrades are installed."""

import pkg_resources
from powerdnsadmin.security.emergency_upgrade import CVEValidator, SecurityException


def main() -> None:
    validator = CVEValidator()
    try:
        validator.validate_all_cves_resolved()
    except SecurityException as exc:
        print(f"Validation failed: {exc}")
        raise SystemExit(1)
    print("All security upgrades validated")


if __name__ == "__main__":
    main()
