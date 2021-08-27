from sqlalchemy import Column, Integer, ForeignKey, Table
from ... import Base

microsoft_scope_uri_connection = Table(
    "microsoft_scope_uri_connection",
    Base.metadata,
    Column(
        "scope_uri_id",
        ForeignKey("microsoft_scope_uri.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
    Column(
        "scope_id",
        ForeignKey("microsoft_scope.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
)
