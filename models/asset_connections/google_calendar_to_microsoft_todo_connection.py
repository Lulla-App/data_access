from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from .. import Base


class GoogleCalendarToMicrosoftTodoConnection(Base):
    __tablename__ = "google_calendar_to_microsoft_todo_connection"

    __table_args__ = (
        UniqueConstraint(
            "from_id", "to_id", name="no_duplicate_connections"
        ),  # TODO solve the duplicate name issue with this constraint
        CheckConstraint(
            "length(from_id) > 0 AND length(to_id) > 0", name="no_empty_string_fields"
        ),
    )

    id = Column("id", Integer, primary_key=True)
    from_id = Column(
        "from_id",
        ForeignKey(
            "managed_google_calendar.external_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
    )
    to_id = Column(
        "to_id",
        ForeignKey(
            "managed_microsoft_todo_task_list.external_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    microsoft_todo_task_list = relationship(
        "ManagedMicrosoftTodoTaskList",
        back_populates="to_microsoft_todo_connections",
    )
    google_calendar = relationship(
        "ManagedGoogleCalendar",
        back_populates="from_google_calendar_connections",
    )
