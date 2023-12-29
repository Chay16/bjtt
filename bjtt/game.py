from random import choice
from typing import Optional

from data.card import Card, Ranks, Suits
from data.hand import Hand
from strategy import strategy, strategy_pair_splitting


def game(double: Optional[bool] = True, das: Optional[bool] = True):
    print("BLACK JACK GAME")
    print(f"'double' : {double}")
    print(f"'double after split' : {double}")
    print("New Hand starting", end="\n" + "-" * 10 + "\n")
    player_hand = Hand(
        Card(choice(Ranks), choice(Suits)), Card(choice(Ranks), choice(Suits))
    )
    dealer_upcard = Card(choice(Ranks), choice(Suits))
    print(f"Your Hand is {player_hand.value} : ({player_hand})")
    print(f"Dealer has {dealer_upcard.value} : ({dealer_upcard})")
    if player_hand.split_available:
        splitting = strategy_pair_splitting(player_hand, dealer_upcard, das=das)
        print(f"Splitting : {splitting}")
        if splitting == "Y":
            player_hands = [Hand(player_hand.cards[0], Card(choice(Ranks), choice(Suits))), Hand(player_hand.cards[1], Card(choice(Ranks), choice(Suits)))]
            print("After splitting your hands are")
            for i, hand in enumerate(player_hands):
                print(f"\tHand-{i+1} {hand.value} : ({hand})")
                print(
                    f"\tYour are playing : {strategy(hand, dealer_upcard, double=double, das=das)}"
                )
        else:
            print(
                f"Your are playing : {strategy(player_hand, dealer_upcard, double=double, das=das)}"
            )
    else:
        print(
            f"Your are playing : {strategy(player_hand, dealer_upcard, double=double, das=das)}"
        )



if __name__ == "__main__":
    game()
