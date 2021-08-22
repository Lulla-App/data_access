from sqlalchemy import Column, String, CheckConstraint
from sqlalchemy.orm import relationship
from . import Base


class ManagedGoogleCalendar(Base):
    __tablename__ = "managed_google_calendar"

    __table_args__ = (
        CheckConstraint(
            "length(external_id) > 0 AND length(external_name) > 0",
            name="no_empty_string_fields",
        ),
    )

    external_id = Column("external_id", String, primary_key=True)
    external_name = Column("external_name", String, nullable=False)

    to_google_calendar_connections = relationship(
        "MicrosoftTodoToGoogleCalendarConnection",
        back_populates="google_calendar",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    from_google_calendar_connections = relationship(
        "GoogleCalendarToMicrosoftTodoConnection",
        back_populates="google_calendar",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self):
        return "ManagedGoogleCalendar(name=%s)" % (self.external_name)


# ManagedGoogleCalendarCalendarParams # TODO when python 3.10 drops
