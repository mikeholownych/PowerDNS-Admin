# Flask 3.x Migration Strategy

This document outlines the approach for migrating PowerDNS-Admin from Flask 2.2 to Flask 3.x.

## Compatibility Assessment

- **Import changes**: `flask.ext.*` imports have long been removed. Extensions should be imported directly (e.g. `from flask_mail import Mail`).
- **Blueprint registration**: Ensure `blueprint.name` is unique and use `app.register_blueprint` with explicit URL prefixes.
- **Request context**: Use `request.get_json()` and `flask.current_app` access patterns.
- **JSON handling**: Switch to `flask.json` provider API where available.
- **Templates**: Jinja2 3 is still supported; ensure custom filters are registered via `app.jinja_env.filters`.
- **Extension compatibility**: See table below.

| Extension | Current Version | Flask 3 Compatible |
|-----------|-----------------|--------------------|
| Flask-SQLAlchemy | 2.5.1 | Use >=3.1 |
| Flask-Login | 0.6.2 | Compatible |
| Flask-Mail | 0.9.1 | Use >=0.9.1 with Flask 3 patches |
| Flask-Migrate | 2.5.3 | Use >=4.0 |
| Flask-Assets | 2.0 | Consider replacement (e.g. Flask-Webpack) |
| Flask-Session | 0.4.0 | Compatible |

## Phased Migration

1. **Compatibility Layer**: added under `powerdnsadmin/compat/` providing helpers abstracting Flask 2/3 differences.
2. **Core Migration**: new `powerdnsadmin/core/` package introducing a modern app factory and blueprint registry.
3. **Extension Updates**: upgrade extensions to Flask 3 compatible versions and wrap legacy APIs in `extension_compat`.

## API Stability

- Decorate endpoints with version-aware decorators.
- Validate request and response formats.
- Emit warnings for deprecated behaviour.
- Expand the test suite to cover API contracts.

## Configuration Management

- Support environment driven configuration with typed classes.
- Validate configuration on startup and integrate secret management.

## Testing Strategy

- Execute tests against Flask 2 and Flask 3 in CI.
- Include performance benchmarking and rollback tests.

## Deployment and Rollback

1. Deploy compatibility layer alongside existing code.
2. Roll forward by enabling Flask 3 in a staging environment.
3. Rollback simply involves reverting to the previous Docker image and database state.
