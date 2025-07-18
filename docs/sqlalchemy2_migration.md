# SQLAlchemy 2.0 Migration Guide

This document describes the approach used to modernise PowerDNS-Admin's ORM
layer to SQLAlchemy 2.0.

## Goals
- Use `DeclarativeBase` with type annotations
- Provide a compatibility layer so existing code continues to run
- Supply migration validators to ensure safe upgrades
- Offer performance tuning guidance

## Zero Downtime Strategy
1. Deploy new code alongside the old using blue/green techniques.
2. Run Alembic migrations with `MigrationValidator` checks.
3. Gradually switch application traffic after validation passes.
4. Roll back automatically if validation fails.

## Performance Optimisation
- Configure SQLAlchemy connection pooling per database backend.
- Use eager loading and `selectinload` to avoid N+1 queries.
- Monitor query latency and create indexes where appropriate.
