"""Run the CVE validator and output a simple report."""

from powerdnsadmin.security.emergency_upgrade import CVEValidator, SecurityException


def main() -> None:
    validator = CVEValidator()
    try:
        validator.validate_all_cves_resolved()
    except SecurityException as exc:
        print(f"Unresolved CVEs detected: {exc}")
        raise SystemExit(1)
    print("All CVEs resolved")


if __name__ == "__main__":
    main()
