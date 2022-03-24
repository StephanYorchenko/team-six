from pydantic import BaseModel


class AccessTokenDTO(BaseModel):
    token: str


class HybridTokenDTO(BaseModel):
    access_token: str
    refresh_token: str
