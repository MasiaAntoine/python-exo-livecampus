from deck import Deck

def main():
    num_players = int(input("Veuillez entrer le nombre de joueurs (2-10): "))
    if num_players < 2 or num_players > 10:
        print("Le nombre de joueurs doit être compris entre 2 et 10.")
        return

    deck = Deck()
    hands, remaining = deck.deal(num_players)

    for i, hand in enumerate(hands):
        print(f"Main du joueur {i + 1} ({len(hand)} cartes): {hand}")
        print("\n")

    if remaining:
        print(f"Cartes restantes ({len(remaining)} cartes): {remaining}")

if __name__ == "__main__":
    main()
