from ..models import (
    ExternalAPISource,
    SessionFactory,
)


def add_external_api_sources_to_database(names):
    with SessionFactory() as session:
        session.add_all([ExternalAPISource(name=n) for n in names])
        session.commit()
