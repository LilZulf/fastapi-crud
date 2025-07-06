from pydantic import BaseModel
from typing import Optional

class MyData(BaseModel):
    name: str
    email: str
    file: Optional[str] = None
    model: Optional[str] = None
