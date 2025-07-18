"""User input validation."""

import re

USERNAME_RE = re.compile(r"^[a-zA-Z0-9_.-]{3,32}$")


def is_valid_username(name: str) -> bool:
    return bool(USERNAME_RE.match(name))
