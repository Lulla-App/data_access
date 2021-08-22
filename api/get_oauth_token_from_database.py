from ..models import (
    OAuthTokens,
    SessionFactory,
)


def get_oauth_token_from_database(service_id):
    with SessionFactory() as session:
        tokens = (
            session.query(OAuthTokens)
            .filter(OAuthTokens.source_name == service_id)
            .one()
        )
        return (tokens.access_token, tokens.refresh_token)
