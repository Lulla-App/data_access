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


def get_all_scopes_from_glue_scope_map(
    scope_map: MicrosoftScopeMap,
) -> set[MS_glue]:
    all_scopes = set()
    for scope_set in scope_map.values():
        all_scopes.update(scope_set)
    return all_scopes


def add_microsoft_oauth_tokens_to_database(oauth_tokens: Iterable[MOAT_glue]):
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
        for token in oauth_tokens:
            try:
                model = MOAT_da(
                    access_token=token.access_token,
                    refresh_token=token.refresh_token,
                    expires_in=token.expires_in,
                    ext_expires_in=token.ext_expires_in,
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


# oauth_token: list[OAuthToken]
"""
The issue of where to have input validation.

it's going to place OAuthToken to TH 

IDing input data that is returned?
How to respond to failure?
JSON Type
What are my conventions and why are they broken

1. Update DA:
user model
how to handle this repo's dependcy on Glue? 
 -> Currently thinking submodules

should I implement mapping of scopes to scope uri's in the database.

2. Implement Database Seeding Script based on glue

make these api independent of sqlalchemy

1. Query all scopes, and map them to their names.
2. Create a TOKEN
3. add scope to token
4. commit the token to database.
"""
