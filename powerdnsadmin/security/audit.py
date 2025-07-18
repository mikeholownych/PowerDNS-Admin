"""Dependency vulnerability scanning using pip-audit."""
from subprocess import run, PIPE

def run_audit(requirements_file: str = "requirements.txt") -> str:
    """Run pip-audit on the provided requirements file and return the report."""
    result = run(["pip-audit", "-r", requirements_file], stdout=PIPE, stderr=PIPE, text=True)
    return result.stdout + result.stderr
