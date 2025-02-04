class Card:
    """
    Classe pour représenter une carte à jouer.

    Attributs:
        suit (str): La couleur de la carte (Coeur, Carreau, Trèfle, Pique).
        rank (str): Le rang de la carte (2-10, Valet, Dame, Roi, As).
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} de {self.suit}"
