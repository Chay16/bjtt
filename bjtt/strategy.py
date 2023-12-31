from typing import Optional

from data.card import Card
from data.counter import Counter
from data.hand import Hand


def strategy_pair_splitting(
    player_hand: Hand, dealer_upcard: Card, counter: Counter, das: Optional[bool] = True
) -> bool:
    if not player_hand.split_available:
        raise ValueError(f"{player_hand} is not splittable")
    if player_hand.cards[0].rank == "A" or player_hand.cards[0].value == 8:
        return True
    elif player_hand.cards[0].value == 10:
        if counter.true_count >= 6 and dealer_upcard.value == 4:
            return True
        elif counter.true_count >= 5 and dealer_upcard.value == 5:
            return True
        elif counter.true_count >= 4 and dealer_upcard.value == 6:
            return True
    elif player_hand.cards[0].value == 9:
        if dealer_upcard.value not in [7, 10, 11]:
            return True
    elif player_hand.cards[0].value == 7:
        if dealer_upcard.value <= 7:
            return True
    elif player_hand.cards[0].value == 6:
        if dealer_upcard.value <= 6:
            if dealer_upcard.value == 2 and das:
                return True
            elif dealer_upcard.value > 2:
                return True
    elif player_hand.cards[0].value == 4 and das:
        if dealer_upcard.value in [5, 6]:
            return True
    elif player_hand.cards[0].value in [2, 3]:
        if 4 <= dealer_upcard.value <= 7:
            return True
        if dealer_upcard.value <= 3 and das:
            return True
    return False


def strategy_soft_totals(
    player_hand: Hand,
    dealer_upcard: Card,
    counter: Counter,
    double: Optional[bool] = True,
) -> str:
    if "A" not in [card.rank for card in player_hand.cards]:
        raise ValueError(f"{player_hand} does not contains one Ace")
    if player_hand.value == 21:
        return "S"
    value = player_hand.value - 11
    if value == 9:
        return "S"
    if value == 8:
        # Deviation
        if dealer_upcard.value == 4:
            if counter.true_count >= 3:
                return "H"
            else:
                return "S"
        elif dealer_upcard.value == 5:
            if counter.true_count >= 1:
                return "H"
            else:
                return "S"
        elif dealer_upcard.value == 6:
            if counter.true_count <= 0:
                return "S"
            else:
                if double:
                    return "D"
                else:
                    return "S"
        else:
            return "S"
    if value == 7:
        if dealer_upcard.value >= 9:
            return "H"
        elif dealer_upcard.value <= 6 and double:
            return "D"
        else:
            return "S"
    if value == 6:
        # Deviation
        if dealer_upcard.value == 2 and counter.true_count >= 1:
            return "S"
        elif 3 <= dealer_upcard.value <= 6 and double:
            return "D"
    if value in [4, 5]:
        if 4 <= dealer_upcard.value <= 6 and double:
            return "D"
    if value in [2, 3]:
        if 5 <= dealer_upcard.value <= 6 and double:
            return "D"
    return "H"


def strategy_hard_totals(
    player_hand: Hand,
    dealer_upcard: Card,
    counter: Counter,
    double: Optional[bool] = True,
):
    # 17 - 18 - 19 - 20 -21
    if 17 <= player_hand.value <= 21:
        return "S"

    # 16
    elif player_hand.value == 16:
        if dealer_upcard.value <= 6:
            return "S"
        elif 7 <= dealer_upcard.value <= 8:
            return "H"
        elif dealer_upcard.value == 9:
            if counter.true_count >= 4:
                return "S"
            else:
                return "H"
        elif dealer_upcard.value == 10:
            if counter.true_count >= 0:
                return "S"
            else:
                return "H"
        else:
            if counter.true_count >= 3:
                return "S"
            else:
                return "H"

    # 15
    elif player_hand.value == 15:
        if dealer_upcard.value <= 6:
            return "S"
        elif 7 <= dealer_upcard.value <= 9:
            return "H"
        elif dealer_upcard.value == 10:
            if counter.true_count >= 4:
                return "S"
            else:
                return "H"
        else:
            if counter.true_count >= 5:
                return "S"
            else:
                return "H"

    # 14
    elif player_hand.value == 14:
        if dealer_upcard.value <= 6:
            return "S"
        else:
            return "H"

    # 13
    elif player_hand.value == 13:
        if dealer_upcard.value == 2:
            if counter.true_count <= -1:
                return "H"
            else:
                return "S"
        elif 3 <= dealer_upcard.value <= 6:
            return "S"
        else:
            return "H"

    # 12
    elif player_hand.value == 12:
        if dealer_upcard.value == 2:
            if counter.true_count >= 3:
                return "S"
            else:
                return "H"
        elif dealer_upcard.value == 3:
            if counter.true_count >= 2:
                return "S"
            else:
                return "H"
        elif dealer_upcard.value == 4:
            if counter.true_count <= 0:
                return "H"
            else:
                return "S"
        elif 5 <= dealer_upcard.value <= 6:
            return "S"
        else:
            return "H"

    # 11
    elif player_hand.value == 11:
        if double:
            return "D"
        else:
            return "H"

    # 10
    elif player_hand.value == 10:
        if dealer_upcard.value <= 9:
            if double:
                return "D"
            else:
                return "H"
        elif dealer_upcard.value == 1:
            if counter.true_count >= 4:
                return "S"
            else:
                return "H"
        else:
            if counter.true_count >= 3:
                return "S"
            else:
                return "H"

    # 9
    elif player_hand.value == 9:
        if dealer_upcard.value == 2:
            if counter.true_count >= 1:
                return "S"
            else:
                return "H"
        elif 3 <= dealer_upcard.value <= 6:
            if double:
                return "D"
            else:
                return "H"
        elif dealer_upcard.value == 7:
            if counter.true_count >= 3:
                return "S"
            else:
                return "H"
        else:
            return "H"
    # 8
    elif player_hand.value == 8:
        if dealer_upcard.value == 6:
            if counter.true_count >= 2:
                return "S"
            else:
                return "H"
        else:
            return "H"

    # 7 - 6 - 5
    else:
        return "H"


def strategy_late_surrender(
    player_hand: Hand, dealer_upcard: Card, counter: Counter
) -> bool:
    if player_hand.value == 17 and dealer_upcard.value == 11:
        return True
    if player_hand.value == 16:
        if dealer_upcard.value == 8:
            if counter.true_count >= 4:
                return True
            else:
                return False
        elif dealer_upcard.value == 9:
            if counter.true_count <= -1:
                return False
            else:
                return True
        elif dealer_upcard.value >= 10:
            return True
        else:
            return False
    if player_hand.value == 15:
        if dealer_upcard.value == 9 and counter.true_count >= 2:
            return True
        elif dealer_upcard.value == 10 and counter.true_count > 0:
            return True
        elif dealer_upcard.value == 11 and counter.true_count >= -1:
            return True
    return False


def strategy(
    player_hand: Hand,
    dealer_upcard: Card,
    counter: Counter,
    double: Optional[bool] = True,
) -> str:
    if player_hand.soft:
        return strategy_soft_totals(player_hand, dealer_upcard, counter, double)
    else:
        return strategy_hard_totals(player_hand, dealer_upcard, counter, double)
