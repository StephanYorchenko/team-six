from pydantic import BaseModel


class AccessToken(BaseModel):
    user_id: str
    access_token: str
    signed: bool = False
