"""Modern app factory leveraging compatibility layer."""

from __future__ import annotations

from flask import Flask
from powerdnsadmin.compat.extension_compat import Mail


def create_app(config_object: str | None = None) -> Flask:
    app = Flask(__name__)
    if config_object:
        app.config.from_object(config_object)

    # Initialize extensions through compatibility wrappers
    Mail(app)

    return app
