from __future__ import annotations

from typing import List
from sqlalchemy.orm import Mapped, relationship

from .base import Base, domain_user_table, account_user_table, domain_apikey_table


class DomainRelationships:
    users: Mapped[List["User"]] = relationship(
        secondary=domain_user_table,
        back_populates="domains",
    )
    apikeys: Mapped[List["ApiKey"]] = relationship(
        secondary=domain_apikey_table,
        back_populates="domains",
    )


class UserRelationships:
    domains: Mapped[List["Domain"]] = relationship(
        secondary=domain_user_table,
        back_populates="users",
    )
    accounts: Mapped[List["Account"]] = relationship(
        secondary=account_user_table,
        back_populates="users",
    )
