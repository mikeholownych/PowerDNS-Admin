"""Shared database base classes and association tables."""

from __future__ import annotations

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, Integer, ForeignKey


db = SQLAlchemy()


class Base(DeclarativeBase):
    """Declarative base used by modern SQLAlchemy 2.0 models."""

    pass


domain_apikey_table = Table(
    "domain_apikey",
    Base.metadata,
    Column("domain_id", Integer, ForeignKey("domain.id")),
    Column("apikey_id", Integer, ForeignKey("apikey.id")),
)


account_user_table = Table(
    "account_user",
    Base.metadata,
    Column("account_id", Integer, ForeignKey("account.id"), nullable=False),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=False),
)


domain_user_table = Table(
    "domain_user",
    Base.metadata,
    Column("domain_id", Integer, ForeignKey("domain.id"), nullable=False),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=False),
)
