from ....models import (
    MicrosoftOAuthToken as MOAT_da,
    SessionFactory,
    MicrosoftScope as MS_da,
    OAuthTokenType as OATT_da,
)
from sqlalchemy import select
from datetime import timedelta
from glue import (
    MicrosoftOAuthToken as MOAT_glue,
    MicrosoftScopeMap,
    MicrosoftScope as MS_glue,
    TokenType as OATT_glue,
)
from typing import Iterable

MOAT_ID = int


def get_all_scopes_from_glue_scope_map(
    scope_map: MicrosoftScopeMap,
) -> set[MS_glue]:
    # TEMP SOLUTION >
    all_scopes = set()
    for scope_set in scope_map.values():
        all_scopes.update(scope_set)
    return all_scopes
    # ^


def update_microsoft_oauth_tokens_in_database(
    oauth_tokens: Iterable[tuple[MOAT_glue, MOAT_ID]]
):
    with SessionFactory() as session:

        # GLOBAL CACHE >
        statement = select(MS_da)
        result = session.execute(statement).scalars().all()
        all_scopes_map = {scope.name: scope for scope in result}
        # ^

        # GLOBAL CACHE >
        statement = select(OATT_da)
        result = session.execute(statement).scalars().all()
        all_token_types_map = {token_type.name: token_type for token_type in result}
        # ^

        for new_token_data, token_id in oauth_tokens:
            statement = select(MOAT_da).filter_by(id=token_id)
            token: MOAT_da = session.execute(statement).scalar_one()

            token.access_token = new_token_data.access_token
            token.refresh_token = new_token_data.refresh_token  # maybe optional
            token.expires_in = new_token_data.expires_in
            token.ext_expires_in = new_token_data.ext_expires_in
            token.token_type = all_token_types_map[new_token_data.token_type.value].id
            token.last_refreshed = new_token_data.created_on

            new_scopes = get_all_scopes_from_glue_scope_map(new_token_data.scopes)

            # scopes = get_all_scopes_from_glue_scope_map(token.scopes)
            for scope in token.scopes:
                if MS_glue(scope.name) not in new_scopes:
                    token.scopes.remove(scope)
            for scope in new_scopes:
                if all_scopes_map[scope.value] not in token.scopes:
                    token.scopes.append(all_scopes_map[scope.value])

            session.commit()
