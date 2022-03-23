from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


async def get_user_from_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    # здесь нужна валидация токена
    return credentials.credentials
