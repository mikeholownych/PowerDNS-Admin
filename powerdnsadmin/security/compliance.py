"""Security compliance checking utilities."""

from datetime import datetime


def check_password_policy(password: str, min_length: int = 12) -> bool:
    """Simple password policy enforcement."""
    return len(password) >= min_length


def log_compliance_event(event: str) -> None:
    """Log a compliance event with timestamp."""
    with open("compliance.log", "a") as fh:
        fh.write(f"{datetime.utcnow().isoformat()} {event}\n")
