from pydantic import BaseModel

class CardCreate(BaseModel):
    suit: str
    rank: str

    class Config:
        orm_mode = True
