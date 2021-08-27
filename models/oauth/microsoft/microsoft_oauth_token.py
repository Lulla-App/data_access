from sqlalchemy import Column, Integer, String, Interval, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ... import Base
from .microsoft_oauth_token_scope_connection import (
    microsoft_oauth_token_scope_connection,
)
import datetime

"""
Desired behavior
Update last_refreshed to current datetime.
this value should always be set by the application server
"""


class MicrosoftOAuthToken(Base):
    __tablename__ = "microsoft_oauth_token"

    id = Column("id", Integer, primary_key=True)
    access_token = Column("access_token", String, nullable=False)
    refresh_token = Column("refresh_token", String, nullable=False)
    expires_in = Column("expires_in", Interval, nullable=False)
    ext_expires_in = Column("ext_expires_in", Interval)
    token_type = Column("token_type", ForeignKey("oauth_token_type.id"), nullable=False)
    last_refreshed = Column(
        "last_refreshed",
        DateTime(),
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )  # This value should always be set as soon as possible

    scopes = relationship(
        "MicrosoftScope",
        secondary=microsoft_oauth_token_scope_connection,
        back_populates="oauth_tokens",
    )
