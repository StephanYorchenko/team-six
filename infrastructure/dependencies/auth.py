from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()


async def get_user_from_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    # TODO: валидация токена
    return credentials.credentials
