"""Create a placeholder system snapshot for rollback."""

import json
from datetime import datetime


def main() -> None:
    snapshot = {"timestamp": datetime.utcnow().isoformat()}
    with open("system-snapshot.json", "w", encoding="utf-8") as fh:
        json.dump(snapshot, fh)
    print("System snapshot created")


if __name__ == "__main__":
    main()
