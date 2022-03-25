from typing import Optional

from pydantic import BaseModel


class AccessToken(BaseModel):
    user_id: str
    access_token: Optional[str]
    signed: bool
