from typing import Optional

from data.card import Card
from data.hand import Hand


def strategy_pair_splitting(
    player_hand: Hand, dealer_upcard: Card, das: Optional[bool] = True
) -> str:
    if not player_hand.split_available:
        raise ValueError(f"{player_hand} is not splittable")
    if player_hand.cards[0].rank == "A" or player_hand.cards[0].value == 8:
        return "Y"
    elif player_hand.cards[0].value == 9:
        if dealer_upcard.value not in [7, 10, 11]:
            return "Y"
    elif player_hand.cards[0].value == 7:
        if dealer_upcard.value <= 7:
            return "Y"
    elif player_hand.cards[0].value == 6:
        if dealer_upcard.value <= 6:
            if dealer_upcard.value == 2 and das:
                return "Y"
            elif dealer_upcard.value > 2:
                return "Y"
    elif player_hand.cards[0].value == 4 and das:
        if dealer_upcard.value in [5, 6]:
            return "Y"
    elif player_hand.cards[0].value in [2, 3]:
        if 4 <= dealer_upcard.value <= 7:
            return "Y"
        if dealer_upcard.value <= 3 and das:
            return "Y"
    return "N"


def strategy_soft_totals(
    player_hand: Hand, dealer_upcard: Card, double: Optional[bool] = True
) -> str:
    if "A" not in [card.rank for card in player_hand.cards]:
        raise ValueError(f"{player_hand} does not contains one Ace")
    if player_hand.value == 21:
        return "S"
    value = player_hand.value - 11
    if value == 9:
        return "S"
    if value == 8:
        print(double)
        if dealer_upcard.value == 6 and double:
            return "D"
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
        if 3 <= dealer_upcard.value <= 6 and double:
            return "D"
    if value in [4, 5]:
        if 4 <= dealer_upcard.value <= 6 and double:
            return "D"
    if value in [2, 3]:
        if 5 <= dealer_upcard.value <= 6 and double:
            return "D"
    return "H"


def strategy_hard_totals(
    player_hand: Hand, dealer_upcard: Card, double: Optional[bool] = True
):
    if 17 <= player_hand.value <= 21:
        return "S"
    if player_hand.value == 11 and double:
        return "D"
    if player_hand.value == 8:
        return "H"
    if dealer_upcard.value <= 6:
        if player_hand.value in [16, 15, 14, 13]:
            return "S"
        elif player_hand.value == 12:
            if dealer_upcard.value <= 3:
                return "H"
            else:
                return "S"
        elif player_hand.value == 10:
            if double:
                return "D"
            else:
                return "H"
        elif player_hand.value == 9:
            if dealer_upcard.value == 2:
                return "H"
            else:
                if double:
                    return "D"
                else:
                    return "H"
    else:
        if player_hand.value >= 12:
            return "H"
        if player_hand.value == 10:
            if dealer_upcard.value <= 9:
                if double:
                    return "D"
                else:
                    return "H"
            else:
                return "H"
    return "H"


def strategy_late_surrender(player_hand: Hand, dealer_upcard: Card) -> bool:
    if player_hand.value == 16 and dealer_upcard.value in [9, 10, 11]:
        return True
    if player_hand.value == 15 and dealer_upcard.value == 10:
        return True
    return False


def strategy(
    player_hand: Hand, dealer_upcard: Card, double: Optional[bool] = True
) -> str:
    if player_hand.soft:
        return strategy_soft_totals(player_hand, dealer_upcard, double)
    else:
        return strategy_hard_totals(player_hand, dealer_upcard, double)
