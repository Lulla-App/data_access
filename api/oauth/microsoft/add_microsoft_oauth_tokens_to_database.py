from ....models import (
    MicrosoftOAuthToken,
    MicrosoftScope,
    SessionFactory,
)
from datetime import timedelta


def add_microsoft_oauth_tokens_to_database(oauth_tokens):
    with SessionFactory() as session:
        for token in oauth_tokens:
            try:
                """
                Add the OAuth data and all of it's scopes
                """
                model = MicrosoftOAuthToken(
                    access_token=token["access_token"],
                    refresh_token=token["refresh_token"],
                    expires_in=token["expires_in"],
                    ext_expires_in=token["ext_expires_in"],
                    token_type=token["token_type"],
                )
                scopes = MicrosoftScope()
                session.add(
                    MicrosoftOAuthToken(
                        access_token=token["access_token"],
                        refresh_token=token["refresh_token"],
                        expires_in=token["expires_in"],
                        ext_expires_in=token["ext_expires_in"],
                        token_type=token["token_type"],
                    )
                )
                session.commit()
            except Exception as e:
                pass


# oauth_token: list[OAuthToken]
"""
The issue of where to have input validation.

it's going to place OAuthToken to TH 

IDing input data that is returned?
How to respond to failure?
JSON Type
What are my conventions and why are they broken
"""
