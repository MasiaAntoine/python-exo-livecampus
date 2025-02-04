import os
try:
    import pytest
except ImportError:
    os.system('pip install pytest')
    import pytest

from deck import Deck

def test_shuffle():
    deck1 = Deck()
    deck2 = Deck()
    deck1.shuffle()
    assert deck1.cards != deck2.cards, "Les paquets ne devraient pas être identiques après mélange."

def test_deal():
    deck = Deck()
    hands, remaining = deck.deal(4)
    assert len(hands) == 4, "Il devrait y avoir 4 mains."
    assert len(remaining) == len(deck.cards) % 4, "Le nombre de cartes restantes devrait être égal au reste de la division du nombre total de cartes par le nombre de joueurs."
    for hand in hands:
        assert len(hand) == len(deck.cards) // 4, "Chaque main devrait avoir un nombre égal de cartes."

def test_invalid_num_players():
    deck = Deck()
    with pytest.raises(ValueError):
        deck.deal(0)
    with pytest.raises(ValueError):
        deck.deal(11)
