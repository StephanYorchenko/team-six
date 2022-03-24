from typing import Optional

from pydantic import BaseModel


class HybridToken(BaseModel):
    user_id: str
    access_token: Optional[str]
    refresh_token: Optional[str]
