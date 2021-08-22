from ..models import Base, engine


def create_database_if_it_doesnt_exist():
    Base.metadata.create_all(engine)
