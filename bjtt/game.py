import argparse
import itertools
from random import choice, shuffle
from typing import List, Optional, Tuple

from data.card import Card, Ranks, Suits
from data.counter import Counter
from data.hand import Hand
from strategy import strategy, strategy_pair_splitting


def params() -> Tuple[int, bool, bool]:
    parser = argparse.ArgumentParser(
        "Black Jack Game", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-decks", type=int, default=4, help="Number of Decks")
    parser.add_argument("--hands", type=int, default=1, help="Number of hands to play")
    parser.add_argument("--no-double", action="store_false", help="No double allowed")
    parser.add_argument(
        "--no-double-after-splitting",
        action="store_false",
        help="No double after splitting allowed",
    )
    params = parser.parse_args()
    return (
        params.decks,
        params.hands,
        params.no_double,
        params.no_double_after_splitting,
    )


def reset_cards() -> List[Card]:
    cards = [
        Card(rank, suit) for rank, suit in list(itertools.product(Ranks, Suits))
    ] * decks
    shuffle(cards)
    return cards


def one_step_strategy(
    cards: List[Card],
    player_hand: Hand,
    dealer_upcard: Card,
    counter: Counter,
    double: bool,
):
    stop = False
    action = strategy(player_hand, dealer_upcard, counter, double)
    if action != "S":
        while action != "S" or not stop:
            if action == "H":
                new_card = cards.pop()
                if len(cards) == 0:
                    cards = reset_cards()
                player_hand.add_card(new_card)
                counter.update(new_card)
                print(f"Action : {action}")
                print(f"Player Hand ({player_hand.value}): {player_hand}")
                print(f"Counter : {counter.true_count}")
                if player_hand.value >= 22:
                    stop = True
                    action = "S"
                else:
                    action = strategy(player_hand, dealer_upcard, counter, double)
            else:
                new_card = cards.pop()
                if len(cards) == 0:
                    cards = reset_cards()
                player_hand.add_card(new_card)
                counter.update(new_card)
                print(f"Action : {action}")
                print(f"Player Hand ({player_hand.value}): {player_hand}")
                stop = True
                action = "S"


def play_strategy(
    player_hand: Hand,
    dealer_upcard: Card,
    counter: Counter,
    double: bool,
    das: bool,
    cards: List[Card],
):
    if player_hand.split_available:
        if strategy_pair_splitting(player_hand, dealer_upcard, counter, das=das):
            print("Split")
            return None
        else:
            one_step_strategy(cards, player_hand, dealer_upcard, counter, double)
            return player_hand.value
    else:
        one_step_strategy(cards, player_hand, dealer_upcard, counter, double)
        return player_hand.value


def play_hand(
    cards: List[Card],
    counter: Counter,
    double: Optional[bool] = True,
    das: Optional[bool] = True,
) -> int:
    print("+" + "-" * 15 + "+")
    print("New Hand Starting")
    print("+" + "-" * 15 + "+")
    global player_hand
    global dealer_hand
    player_hand_card1 = cards.pop()
    if len(cards) == 0:
        cards = reset_cards()
    counter.update(player_hand_card1)
    dealer_upcard = cards.pop()
    if len(cards) == 0:
        cards = reset_cards()
    counter.update(dealer_upcard)
    player_hand = Hand(player_hand_card1, cards.pop())
    if len(cards) == 0:
        cards = reset_cards()
    counter.update(player_hand.cards[-1])
    dealer_hand = Hand(dealer_upcard, cards.pop())
    if len(cards) == 0:
        cards = reset_cards()
    counter.update(dealer_hand.cards[-1])
    print(f"Player Hand ({player_hand.value}): {player_hand}")
    print(f"Dealer Upcard ({dealer_upcard.value}) : {dealer_upcard}")
    print(f"Counter : {counter.true_count}")
    if player_hand.value == 21:
        print(f"Dealer Hand ({dealer_hand.value}) : {dealer_hand}")
        print("BLACK JACK !")
        print("+" + "-" * 15 + "+\n")
        return 2
    else:
        play_strategy(player_hand, dealer_upcard, counter, double, das, cards)
    print(f"Final Player Hand ({player_hand.value}) : {player_hand}")
    print(f"Dealer Hand ({dealer_hand.value}) : {dealer_hand}")
    while dealer_hand.value < 17:
        dealer_hand.add_card(cards.pop())
    print(f"Final Dealer Hand ({dealer_hand.value}) : {dealer_hand}")
    print("")
    if dealer_hand.value >= player_hand.value:
        print("LOST")
        print("+" + "-" * 15 + "+\n")
        return 0
    else:
        print("WIN")
        print("+" + "-" * 15 + "+\n")
        return 1


def game(
    decks: int, hands: int, double: Optional[bool] = True, das: Optional[bool] = True
):
    print("\n" + "=" * 15)
    print("BLACK JACK GAME")
    print("=" * 15)
    print(f"Decks : {decks}")
    print(f"'double' : {double}")
    print(f"'double after split' : {double}")
    print(f"Starting {hands} hands plays")
    print("")
    global all_cards
    all_cards = reset_cards()
    global counter
    counter = Counter(decks)
    hands_results = {"Win": 0, "Lost": 0}
    for i in range(hands):
        result = play_hand(all_cards, counter, double, das)
        if result == 1:
            hands_results["Win"] += 1
        else:
            hands_results["Lost"] += 1
    if hands > 1:
        print(f"{hands} Hands Summary")
        print(hands_results)
        print(
            f"Win Percentage : {hands_results['Win']/sum(hands_results.values()):.2%}"
        )


if __name__ == "__main__":
    global decks
    decks, hands, double, double_after_splitting = params()
    game(decks, hands, double, double_after_splitting)
