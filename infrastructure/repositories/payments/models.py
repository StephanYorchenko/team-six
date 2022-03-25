from typing import Optional

from pydantic import BaseModel


class Payment(BaseModel):
    id: str
    crm_id: str
    title: str
    description: Optional[str] = ''
    amount: float
    created_at: str
    partnerId: str
    processed: bool