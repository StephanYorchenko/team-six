from typing import Optional, Dict

from pydantic import BaseModel


class Payment(BaseModel):
    id: int
    crm_id: str
    title: str
    description: Optional[str] = ''
    amount: float
    created_at: str


#Special classes which needs to create payment json object


class InstructedAmount(BaseModel):
    amount: str
    currency: str="RUB"


class CreditorAccount(BaseModel):
    schemeName: str = "RU.CBR.PAN"
    identification: str
    name: str


class RemittanceInformation(BaseModel):
    unstructured: str
    reference: str


class Initiation(BaseModel):
    instructionIdentification: str = "PISP412"
    endToEndIdentification: str = "MERCHANT.256702.IDN.12"
    InstructedAmount: InstructedAmount
    CreditorAccount: CreditorAccount
    RemittanceInformation: RemittanceInformation


class Data(BaseModel):
    Initiation: Initiation
#That' s all


class PaymentJson(BaseModel):
    Data: Data
    Risk: Dict[] = {}


headers = {
  'x-idempotency-key': '5214b9e0-2e24-4f93-835a-20ed99b5471a',
  'Accept': 'application/json',
  'x-jws-signature': '',
  'Authorization': 'Bearer ',
  'Content-Type': 'application/json'
}




