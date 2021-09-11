from sqlalchemy import Column, Integer, String, Interval, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ... import Base
from .google_oauth_token_scope_correlation import (
    google_oauth_token_scope_correlation,
)
import datetime

"""
Desired behavior
Update last_refreshed to current datetime.
this value should always be set by the application server
"""


class GoogleOAuthToken(Base):
    __tablename__ = "google_oauth_token"

    id = Column("id", Integer, primary_key=True)
    access_token = Column("access_token", String, nullable=False)
    refresh_token = Column("refresh_token", String, nullable=False)
    expires_in = Column("expires_in", Interval, nullable=False)
    token_type = Column("token_type", ForeignKey("oauth_token_type.id"), nullable=False)
    last_refreshed = Column(
        "last_refreshed",
        DateTime(),
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )  # This value should always be set as soon as possible

    scopes = relationship(
        "GoogleScope",
        secondary=google_oauth_token_scope_correlation,
        back_populates="oauth_tokens",
    )
    token = relationship("OAuthTokenType")
