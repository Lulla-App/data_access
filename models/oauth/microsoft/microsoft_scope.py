from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ... import Base
from .microsoft_oauth_token_scope_connection import (
    microsoft_oauth_token_scope_connection,
)
from .microsoft_scope_uri_connection import microsoft_scope_uri_connection


class MicrosoftScope(Base):
    __tablename__ = "microsoft_scope"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False, unique=True)

    oauth_tokens = relationship(
        "MicrosoftOAuthToken",
        secondary=microsoft_oauth_token_scope_connection,
        back_populates="scopes",
    )  # this field seems like it might be kind of dangerous
    uris = relationship(
        "MicrosoftScopeUri",
        secondary=microsoft_scope_uri_connection,
        back_populates="scopes",
    )
