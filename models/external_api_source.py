from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base


class ExternalAPISource(Base):
    __tablename__ = "external_api_source"

    name = Column("name", String(50), primary_key=True, unique=True, nullable=False)
    auth_data = relationship("OAuthTokens")


# ExternalAPISourceParams # TODO when python 3.10 drops
