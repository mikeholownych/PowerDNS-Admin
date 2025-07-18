from __future__ import annotations

"""Modern SQLAlchemy 2.0 query helpers."""

from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session

from powerdnsadmin.models.user import User


def get_user_by_email(session: Session, email: str) -> Optional[User]:
    stmt = select(User).where(User.email == email)
    return session.scalars(stmt).first()
