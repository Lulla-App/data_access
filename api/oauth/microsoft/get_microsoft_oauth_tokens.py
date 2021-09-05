from ....models import (
    MicrosoftOAuthToken as MOAT_da,
    SessionFactory,
    MicrosoftScope as MS_da,
    OAuthTokenType as OATT_da,
)
from glue import (
    MicrosoftOAuthToken as MOAT_glue,
    MicrosoftScopeMap,
    MicrosoftScope as MS_glue,
    TokenType as OATT_glue,
)
from sqlalchemy import select


def convert_microsoft_oauth_token_from_da_to_glue_model(
    microsoft_oauth_token: MOAT_da,
) -> MOAT_glue:
    glue_oauth_token = MOAT_glue(
        access_token=microsoft_oauth_token.access_token,
        refresh_token=microsoft_oauth_token.refresh_token,
        expires_in=microsoft_oauth_token.expires_in,
        ext_expires_in=microsoft_oauth_token.ext_expires_in,
        token_type=OATT_glue(microsoft_oauth_token.token.name),
    )
    # TEMP SOLUTION >
    for scope in microsoft_oauth_token.scopes:
        glue_oauth_token.scopes.add(MS_glue(scope.name))
    # ^
    return glue_oauth_token


def get_microsoft_oauth_tokens() -> list[tuple[MOAT_glue, int]]:
    with SessionFactory() as session:
        statement = select(MOAT_da)
        oauth_tokens: list[MOAT_da] = session.execute(statement).scalars().all()

        return list(
            map(
                lambda oauth_token: (
                    convert_microsoft_oauth_token_from_da_to_glue_model(oauth_token),
                    oauth_token.id,
                ),
                oauth_tokens,
            )
        )
