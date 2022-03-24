from pydantic import BaseModel


class AccessTokenDTO(BaseModel):
    token: str


class HybridAccessTokenDTO(BaseModel):
    token: str


class HybridRefreshToken(BaseModel):
    token: str
