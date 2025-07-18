"""Runtime security monitoring stubs."""

import logging

logger = logging.getLogger(__name__)


def log_security_event(event: str) -> None:
    """Log a security event."""
    logger.info("SECURITY EVENT: %s", event)
