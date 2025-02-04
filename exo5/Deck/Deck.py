import random
from Card.Card import Card

class Deck:
    """
    Classe pour représenter un paquet de 52 cartes.

    Attributs:
        cards (list): Liste des cartes dans le paquet.
    """
    suits = ["Coeur", "Carreau", "Trèfle", "Pique"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        """
        Mélange le paquet de cartes.
        """
        random.shuffle(self.cards)

    def deal(self, num_players):
        """
        Distribue équitablement les cartes à plusieurs joueurs.

        Args:
            num_players (int): Le nombre de joueurs.

        Returns:
            tuple: Liste de listes de cartes pour chaque joueur et liste des cartes restantes.
        """
        if num_players <= 0 or num_players > 10:
            raise ValueError("Le nombre de joueurs doit être compris entre 1 et 10.")

        self.shuffle()
        hands = [[] for _ in range(num_players)]
        cards_per_player = len(self.cards) // num_players
        remaining_cards = len(self.cards) % num_players

        for i in range(cards_per_player * num_players):
            hands[i % num_players].append(self.cards[i])

        remaining = self.cards[cards_per_player * num_players:]

        return hands, remaining
