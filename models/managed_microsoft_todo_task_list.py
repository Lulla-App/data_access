from sqlalchemy import Column, String, CheckConstraint
from sqlalchemy.orm import relationship
from . import Base


class ManagedMicrosoftTodoTaskList(Base):
    __tablename__ = "managed_microsoft_todo_task_list"

    __table_args__ = (
        CheckConstraint(
            "length(external_id) > 0 AND length(external_name) > 0",
            name="no_empty_string_fields",
        ),
    )

    external_id = Column("external_id", String, primary_key=True)
    external_name = Column("external_name", String, nullable=False)

    to_microsoft_todo_connections = relationship(
        "GoogleCalendarToMicrosoftTodoConnection",
        back_populates="microsoft_todo_task_list",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    from_microsoft_todo_connections = relationship(
        "MicrosoftTodoToGoogleCalendarConnection",
        back_populates="microsoft_todo_task_list",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self):
        return "ManagedMicrosoftToDoTaskList(name=%s)" % (self.external_name)


# ManagedMicrosoftToDoTaskListParams # TODO when python 3.10 drops
