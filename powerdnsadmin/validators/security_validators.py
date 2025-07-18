"""Security-related input validation."""

MAX_REQUEST_SIZE = 1024 * 1024  # 1MB


def enforce_request_size(data: bytes) -> bool:
    return len(data) <= MAX_REQUEST_SIZE
