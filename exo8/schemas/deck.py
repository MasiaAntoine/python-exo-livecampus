from pydantic import BaseModel
from schemas.card import CardCreate

class DeckCreate(BaseModel):
    cards: list[CardCreate]

    class Config:
        orm_mode = True
