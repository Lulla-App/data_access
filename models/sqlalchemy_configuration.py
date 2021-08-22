from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry, DeclarativeMeta
import os

# Configure Engine
"""
https://docs.sqlalchemy.org/en/14/core/engines.html
https://www.python.org/dev/peps/pep-0249/
"""
engine = create_engine(os.environ["DATABASE_URL"], echo=True)

# Configure Session
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

# Configure Mapper
mapper_registry = registry()

# Configure Base
class Base(metaclass=DeclarativeMeta):
    __abstract__ = True

    registry = mapper_registry
    metadata = mapper_registry.metadata
