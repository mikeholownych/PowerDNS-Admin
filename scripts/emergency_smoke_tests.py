"""Run minimal smoke tests after emergency upgrades."""

import subprocess


def main() -> None:
    result = subprocess.run(["pytest", "tests/security", "-q"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
