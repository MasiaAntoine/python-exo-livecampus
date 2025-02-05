from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class CardModel(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True)
    suit = Column(String, index=True)
    rank = Column(String, index=True)
    deck_id = Column(Integer, ForeignKey('decks.id'))

    deck = relationship("DeckModel", back_populates="cards")
