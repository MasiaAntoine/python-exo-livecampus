from fastapi import FastAPI, HTTPException
from Deck.Deck import Deck

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur FastAPI"}

@app.get("/deck")
def get_deck():
    deck = Deck()
    return {"deck": deck.cards}

@app.get("/deal/{num_players}")
def deal_cards(num_players: int):
    if num_players < 2 or num_players > 10:
        raise HTTPException(status_code=400, detail="Le nombre de joueurs doit être compris entre 2 et 10.")

    deck = Deck()
    hands, remaining = deck.deal(num_players)
    return {"hands": hands, "remaining": remaining}
