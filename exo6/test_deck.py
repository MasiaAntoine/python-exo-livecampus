import unittest
from deck import Deck

class TestDeck(unittest.TestCase):
    def test_shuffle(self):
        deck1 = Deck()
        deck2 = Deck()
        deck1.shuffle()
        self.assertNotEqual(deck1.cards, deck2.cards, "Les paquets ne devraient pas être identiques après mélange.")

    def test_deal(self):
        deck = Deck()
        hands, remaining = deck.deal(4)
        self.assertEqual(len(hands), 4, "Il devrait y avoir 4 mains.")
        self.assertEqual(len(remaining), len(deck.cards) % 4, "Le nombre de cartes restantes devrait être égal au reste de la division du nombre total de cartes par le nombre de joueurs.")
        for hand in hands:
            self.assertEqual(len(hand), len(deck.cards) // 4, "Chaque main devrait avoir un nombre égal de cartes.")

    def test_invalid_num_players(self):
        deck = Deck()
        with self.assertRaises(ValueError):
            deck.deal(0)
        with self.assertRaises(ValueError):
            deck.deal(11)

if __name__ == '__main__':
    unittest.main()
