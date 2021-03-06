from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ... import Base
from .microsoft_scope_uri_correlation import microsoft_scope_uri_correlation


class MicrosoftScopeUri(Base):
    __tablename__ = "microsoft_scope_uri"

    id = Column("id", Integer, primary_key=True)
    uri = Column("uri", String, nullable=False, unique=True)

    scopes = relationship(
        "MicrosoftScope",
        secondary=microsoft_scope_uri_correlation,
        back_populates="uris",
    )
