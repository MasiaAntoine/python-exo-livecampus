from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from db import Base

class DeckModel(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True, index=True)
    cards = relationship("CardModel", back_populates="deck")
