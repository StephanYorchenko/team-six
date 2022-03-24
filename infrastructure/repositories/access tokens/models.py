from pydantic import BaseModel
from typing import Optional


class AccessToken(BaseModel):
    user_id: str
    access_token: Optional[str]
    validate: bool
