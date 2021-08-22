from sqlalchemy import Column, Integer, String, ForeignKey
from . import Base


class OAuthTokens(Base):
    __tablename__ = "oauth_tokens"

    source_name = Column(
        "source_name", ForeignKey("external_api_source.name"), primary_key=True
    )
    access_token = Column("access_token", String)
    refresh_token = Column("refresh_token", String)


# OAuthTokensParams # TODO when python 3.10 drops
