from sqlalchemy import Column, Integer, ForeignKey, Table
from ... import Base

google_scope_uri_correlation = Table(
    "google_scope_uri_correlation",
    Base.metadata,
    Column(
        "scope_uri_id",
        ForeignKey("google_scope_uri.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
    Column(
        "scope_id",
        ForeignKey("google_scope.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
)
