from typing import Optional

from pydantic import BaseModel


class PaymentInputDTO(BaseModel):
    crm_id: int


class PaymentOutputDTO(BaseModel):
    title: str
    description: Optional[str]
    created_at: str
    amount: float
    logo_url: Optional[str]
    processed: bool = False


class Payment(PaymentOutputDTO):
    ...
