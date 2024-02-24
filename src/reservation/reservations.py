from pydantic import BaseModel


class Reservation(BaseModel):
    id: str
