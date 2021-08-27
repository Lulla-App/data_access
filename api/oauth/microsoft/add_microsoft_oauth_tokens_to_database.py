from ....models import MicrosoftOAuthToken, MicrosoftScope, SessionFactory, engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import timedelta
from ....glue import MicrosoftOAuthToken as MAT_glue
from typing import Iterable


def get_all_scopes_from_glue_scope_map(
    scope_map: MicrosoftScopeMap,
) -> set[MicrosoftScope]:
    all_scopes = set()
    for scope_set in scope_map.values():
        all_scopes.update(scope_set)
    return all_scopes


def add_microsoft_oauth_tokens_to_database(oauth_tokens: Iterable[MAT_glue]):
    with SessionFactory() as session:

        statement = select(MicrosoftScope)
        result = session.execute(statement).scalars().all()
        all_scopes_map = {scope.name: scope for scope in result}

        for token in oauth_tokens:
            try:
                model = MicrosoftOAuthToken(
                    access_token=token.access_token,
                    refresh_token=token.refresh_token,
                    expires_in=token.expires_in,
                    ext_expires_in=token.ext_expires_in,
                    token_type=token.token_type.value,
                )

                scopes = get_all_scopes_from_glue_scope_map(token.scopes)
                for scope in scopes:
                    model.scopes.add(all_scopes_map[scope.value])

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
