from ..models import (
    GoogleCalendarToMicrosoftTodoConnection,
    MicrosoftTodoToGoogleCalendarConnection,
    SessionFactory,
)


def add_connections_to_database(connections):
    statuses = []
    with SessionFactory() as session:
        for connection in connections:
            status = ""
            try:
                if connection["connection_type"] == "google_calendar_to_microsoft_todo":
                    session.add(
                        GoogleCalendarToMicrosoftTodoConnection(
                            from_id=connection["from_id"], to_id=connection["to_id"]
                        )
                    )
                elif (
                    connection["connection_type"] == "microsoft_todo_to_google_calendar"
                ):
                    session.add(
                        MicrosoftTodoToGoogleCalendarConnection(
                            from_id=connection["from_id"], to_id=connection["to_id"]
                        )
                    )

                session.commit()
                status = "success"
            except Exception as e:
                status = "failure"

            statuses.append({"status": status, "object": connection})

    return statuses
