from __future__ import annotations

from sqlalchemy.types import TypeDecorator, String


class EmailType(TypeDecorator):
    """Custom type for storing email addresses with basic validation."""

    impl = String(255)

    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value.lower()
