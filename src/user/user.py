from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str
    surname: str
    phone_number: int
