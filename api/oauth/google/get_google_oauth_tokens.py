from ....models import (
    GoogleOAuthToken as GOAT_da,
    SessionFactory,
    GoogleScope as GS_da,
    OAuthTokenType as OATT_da,
)
from glue import (
    GoogleOAuthToken as GOAT_glue,
    GoogleScopeMap,
    GoogleScope as GS_glue,
    TokenType as OATT_glue,
)
from sqlalchemy import select


def convert_google_oauth_token_from_da_to_glue_model(
    google_oauth_token: GOAT_da,
) -> GOAT_glue:
    glue_oauth_token = GOAT_glue(
        access_token=google_oauth_token.access_token,
        refresh_token=google_oauth_token.refresh_token,
        expires_in=google_oauth_token.expires_in,
        token_type=OATT_glue(google_oauth_token.token.name),
    )
    # TEMP SOLUTION >
    for scope in google_oauth_token.scopes:
        glue_oauth_token.scopes.add(GS_glue(scope.name))
    # ^
    return glue_oauth_token


def get_google_oauth_tokens() -> list[tuple[GOAT_glue, int]]:
    with SessionFactory() as session:
        statement = select(GOAT_da)
        oauth_tokens: list[GOAT_da] = session.execute(statement).scalars().all()

        return list(
            map(
                lambda oauth_token: (
                    convert_google_oauth_token_from_da_to_glue_model(oauth_token),
                    oauth_token.id,
                ),
                oauth_tokens,
            )
        )
