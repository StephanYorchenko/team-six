from typing import Optional

from pydantic import BaseModel


class Payment(BaseModel):
    id: int
    crm_id: str
    title: str
    description: Optional[str] = ''
    amount: float
    created_at: str
