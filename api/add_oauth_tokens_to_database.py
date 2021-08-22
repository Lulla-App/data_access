from ..models import (
    OAuthTokens,
    SessionFactory,
)


def add_oauth_tokens_to_database(oauth_data):
    with SessionFactory() as session:
        session.add_all([OAuthTokens(**datum) for datum in oauth_data])
        session.commit()
