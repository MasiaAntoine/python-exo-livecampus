from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from Deck.Deck import Deck
from db import get_db
from models.card import CardModel
from models.deck import DeckModel
from schemas.card import CardCreate
from schemas.deck import DeckCreate

app = FastAPI()

@app.post("/cards/", response_model=CardCreate)
def create_card(card: CardCreate, db: Session = Depends(get_db)):
    db_card = CardModel(suit=card.suit, rank=card.rank)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

@app.get("/cards/")
def read_cards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cards = db.query(CardModel).offset(skip).limit(limit).all()
    return cards

@app.get("/cards/{card_id}")
def read_card(card_id: int, db: Session = Depends(get_db)):
    card = db.query(CardModel).filter(CardModel.id == card_id).first()
    if card is None:
        raise HTTPException(status_code=404, detail="Carte non trouvée")
    return card

@app.delete("/cards/{card_id}")
def delete_card(card_id: int, db: Session = Depends(get_db)):
    card = db.query(CardModel).filter(CardModel.id == card_id).first()
    if card is None:
        raise HTTPException(status_code=404, detail="Carte non trouvée")
    db.delete(card)
    db.commit()
    return {"detail": "Carte supprimée"}

@app.post("/deck/", response_model=DeckCreate)
def create_deck(db: Session = Depends(get_db)):
    deck = Deck()
    db_deck = DeckModel()
    db.add(db_deck)
    db.commit()
    db.refresh(db_deck)
    for card in deck.cards:
        db_card = CardModel(suit=card.suit, rank=card.rank, deck_id=db_deck.id)
        db.add(db_card)
    db.commit()
    return {"cards": [CardCreate(suit=card.suit, rank=card.rank) for card in deck.cards]}

@app.get("/deck/")
def get_deck(db: Session = Depends(get_db)):
    decks = db.query(DeckModel).all()
    return {"decks": decks}
