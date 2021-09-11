from sqlalchemy import Column, Integer, ForeignKey, Table
from ... import Base

google_oauth_token_scope_correlation = Table(
    "google_oauth_token_scope_correlation",
    Base.metadata,
    Column(
        "oauth_token_id",
        ForeignKey("google_oauth_token.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
    Column(
        "scope_id",
        ForeignKey("google_scope.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
)
