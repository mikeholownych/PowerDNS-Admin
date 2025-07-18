import pkg_resources


def _get_version(pkg_name: str) -> str:
    return pkg_resources.get_distribution(pkg_name).version


def test_flask_session_security():
    assert _get_version("Flask") == "2.3.3"


def test_jinja2_sandbox_security():
    assert _get_version("Jinja2") == "3.1.6"


def test_werkzeug_security_fixes():
    assert _get_version("werkzeug") == "2.3.8"


def test_requests_ssl_verification():
    assert _get_version("requests") == "2.32.3"


def test_gunicorn_request_smuggling_protection():
    assert _get_version("gunicorn") == "23.0.0"
