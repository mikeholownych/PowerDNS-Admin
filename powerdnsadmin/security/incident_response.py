"""Security incident response stubs."""

from datetime import datetime


def create_incident_report(summary: str) -> str:
    """Create a simple incident report entry."""
    timestamp = datetime.utcnow().isoformat()
    return f"{timestamp}: {summary}"
