from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ... import Base
from .google_oauth_token_scope_correlation import (
    google_oauth_token_scope_correlation,
)
from .google_scope_uri_correlation import google_scope_uri_correlation


class GoogleScope(Base):
    __tablename__ = "google_scope"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False, unique=True)

    oauth_tokens = relationship(
        "GoogleOAuthToken",
        secondary=google_oauth_token_scope_correlation,
        back_populates="scopes",
    )  # this field seems like it might be kind of dangerous
    uris = relationship(
        "GoogleScopeUri",
        secondary=google_scope_uri_correlation,
        back_populates="scopes",
    )
