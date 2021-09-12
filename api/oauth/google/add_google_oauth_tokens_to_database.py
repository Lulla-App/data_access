from ....models import (
    GoogleOAuthToken as GOAT_da,
    SessionFactory,
    GoogleScope as GS_da,
    OAuthTokenType as OATT_da,
)
from sqlalchemy import select
from datetime import timedelta
from glue import (
    GoogleOAuthToken as GOAT_glue,
    GoogleScopeMap,
    GoogleScope as GS_glue,
    TokenType as OATT_glue,
)
from typing import Iterable


def get_all_scopes_from_glue_scope_map(
    scope_map: GoogleScopeMap,
) -> set[GS_glue]:
    all_scopes = set()
    for scope_set in scope_map.values():
        all_scopes.update(scope_set)
    return all_scopes


def add_google_oauth_tokens_to_database(oauth_tokens: Iterable[GOAT_glue]):
    with SessionFactory() as session:
        # GLOBAL CACHE >
        statement = select(GS_da)
        result = session.execute(statement).scalars().all()
        all_scopes_map = {scope.name: scope for scope in result}
        # ^

        # GLOBAL CACHE >
        statement = select(OATT_da)
        result = session.execute(statement).scalars().all()
        all_token_types_map = {token_type.name: token_type for token_type in result}
        # ^
        for token in oauth_tokens:
            try:
                model = GOAT_da(
                    access_token=token.access_token,
                    refresh_token=token.refresh_token,
                    expires_in=token.expires_in,
                    token_type=all_token_types_map[token.token_type.value].id,
                    last_refreshed=token.created_on,
                )

                scopes = get_all_scopes_from_glue_scope_map(token.scopes)
                for scope in scopes:
                    model.scopes.append(all_scopes_map[scope.value])

                session.add(model)
                session.commit()
            except Exception as e:
                pass
