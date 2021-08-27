from sqlalchemy import Column, String, Integer
from .. import Base


class OAuthTokenType(Base):
    __tablename__ = "oauth_token_type"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False, unique=True)
