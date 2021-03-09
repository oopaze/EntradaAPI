from datetime import datetime
from pydantic import BaseModel


class EntradaSchema(BaseModel):
    link: str
    action: str
    update_id: int
    data: datetime = None

    class Config:
        orm_mode = True