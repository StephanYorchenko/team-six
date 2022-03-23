from pydantic import BaseModel


class UserInputDTO(BaseModel):
    identifier: str


class UserOutputDTO(BaseModel):
    login: str
