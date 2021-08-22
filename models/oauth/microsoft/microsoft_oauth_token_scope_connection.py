from sqlalchemy import Column, Integer, ForeignKey, Table
from ... import Base

microsoft_oauth_token_scope_connection = Table(
    "microsoft_oauth_token_scope_connection",
    Base.metadata,
    Column(
        "oauth_token_id",
        ForeignKey("microsoft_oauth_token.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
    Column(
        "scope_id",
        ForeignKey("microsoft_scope.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
)
