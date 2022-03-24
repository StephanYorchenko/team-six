from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()


async def get_user_from_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    if not (user := credentials.credentials):
        raise Exception('Authorization is required')
    return user
