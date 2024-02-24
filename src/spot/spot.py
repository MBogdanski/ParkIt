from typing import Union, Any

import uuid as uuid
from pydantic import BaseModel


class Spot(BaseModel):
    id: uuid.UUID
    number: int
    level: int
    is_available: Union[bool, None] = None

    def __init__(self, number: int, level: int, is_available: bool, /, **data: Any):
        super().__init__(id=uuid.uuid4(), number=number, level=level, is_available=is_available, **data)
