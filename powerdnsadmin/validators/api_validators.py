"""API input validation."""

from .security_validators import enforce_request_size


def validate_api_key(key: str) -> bool:
    return len(key) >= 32
