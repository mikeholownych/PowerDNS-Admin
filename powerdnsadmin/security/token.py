"""Session and API token utilities."""

import secrets


def generate_token(length: int = 32) -> str:
    """Return a secure random URL-safe token."""
    return secrets.token_urlsafe(length)
