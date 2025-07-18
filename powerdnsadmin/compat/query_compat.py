"""Legacy query wrappers used during the migration to SQLAlchemy 2.0."""
from __future__ import annotations

from typing import Optional, Type, TypeVar
from sqlalchemy import select
from sqlalchemy.orm import Session

T = TypeVar("T")


def first_by(session: Session, model: Type[T], **kwargs) -> Optional[T]:
    """Replicates old ``Model.query.filter_by().first()`` pattern."""
    stmt = select(model).filter_by(**kwargs)
    return session.scalars(stmt).first()
