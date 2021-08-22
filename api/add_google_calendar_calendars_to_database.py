from ..models import (
    ManagedGoogleCalendar,
    SessionFactory,
)


def add_google_calendar_calendars_to_database(calendar_data):
    with SessionFactory() as session:
        session.add_all([ManagedGoogleCalendar(**datum) for datum in calendar_data])
        session.commit()
