from typing import Optional

from pydantic import BaseModel, Field


class Payment(BaseModel):
    identifier: Optional[str]
    title: str
    description: Optional[str]
    created_at: str = Field(..., alias="createdAt")
    amount: float
    processed: bool = False

    partnerId: str


class Partner(BaseModel):
    identifier: Optional[str]
    fullName: Optional[str]
    logoUrl: Optional[str]
    taxCode: Optional[str]
    kpp: Optional[str]
