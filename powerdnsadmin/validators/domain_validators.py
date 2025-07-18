"""DNS-specific validation helpers."""

import re

DOMAIN_RE = re.compile(r"^(?:[a-zA-Z0-9-]{,63}\.)+[a-zA-Z]{2,}$")


def is_valid_domain(name: str) -> bool:
    return bool(DOMAIN_RE.match(name))
