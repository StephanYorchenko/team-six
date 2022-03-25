from pydantic import BaseModel


class Partner(BaseModel):
    identifier: str
    fullName: str
    logoUrl: str
