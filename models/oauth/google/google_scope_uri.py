from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ... import Base
from .google_scope_uri_correlation import google_scope_uri_correlation


class GoogleScopeUri(Base):
    __tablename__ = "google_scope_uri"

    id = Column("id", Integer, primary_key=True)
    uri = Column("uri", String, nullable=False, unique=True)

    scopes = relationship(
        "GoogleScope",
        secondary=google_scope_uri_correlation,
        back_populates="uris",
    )
