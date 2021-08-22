from ..models import (
    ManagedMicrosoftTodoTaskList,
    SessionFactory,
)


def add_microsoft_todo_lists_to_database(task_list_data):
    with SessionFactory() as session:
        session.add_all(
            [ManagedMicrosoftTodoTaskList(**datum) for datum in task_list_data]
        )
        session.commit()
