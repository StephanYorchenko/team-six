from typing import Optional

from pydantic import BaseModel


class Payment(BaseModel):
    identifier: int
    crm_id: str
    title: str
    description: Optional[str] = ""
    amount: float
    created_at: str
