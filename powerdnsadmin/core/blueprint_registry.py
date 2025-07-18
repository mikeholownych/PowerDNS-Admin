"""Blueprint registration utilities."""

from __future__ import annotations

from flask import Flask


class BlueprintRegistry:
    def __init__(self, app: Flask):
        self.app = app
        self.blueprints = []

    def register(self, blueprint, url_prefix: str | None = None) -> None:
        self.app.register_blueprint(blueprint, url_prefix=url_prefix)
        self.blueprints.append(blueprint)
