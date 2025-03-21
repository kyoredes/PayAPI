from fastapi_users.authentication import AuthenticationBackend
from payapi.authentication.dependencies.transport import bearer_transport
from payapi.authentication.dependencies.strategy import get_db_strategy


auth_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_db_strategy,
)
