from data.card import Card, Ranks
from data.hand import Hand
from pytest import raises
from strategy import (
    strategy,
    strategy_late_surrender,
    strategy_pair_splitting,
    strategy_soft_totals,
)


def test_pair_splitting():
    # No Split
    hand_nosplit = Hand(Card("A", "H"), Card("2", "D"))
    with raises(ValueError):
        strategy_pair_splitting(hand_nosplit, Card("A", "H"))

    # Split
    hand_aces = Hand(Card("A", "H"), Card("A", "D"))
    hand_head = Hand(Card("K", "H"), Card("K", "D"))
    hand_9s = Hand(Card("9", "H"), Card("9", "D"))
    hand_8s = Hand(Card("8", "H"), Card("8", "D"))
    hand_7s = Hand(Card("7", "H"), Card("7", "D"))
    hand_6s = Hand(Card("6", "H"), Card("6", "D"))
    hand_5s = Hand(Card("5", "H"), Card("5", "D"))
    hand_4s = Hand(Card("4", "H"), Card("4", "D"))
    hand_3s = Hand(Card("3", "H"), Card("3", "D"))
    hand_2s = Hand(Card("2", "H"), Card("2", "D"))

    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        assert strategy_pair_splitting(hand_aces, dealer_upcard) == "Y"
        assert strategy_pair_splitting(hand_head, dealer_upcard) == "N"
        assert strategy_pair_splitting(hand_8s, dealer_upcard) == "Y"
        assert strategy_pair_splitting(hand_5s, dealer_upcard) == "N"
        if Card(rank, "H").value <= 6:
            assert strategy_pair_splitting(hand_9s, dealer_upcard) == "Y"
            assert strategy_pair_splitting(hand_7s, dealer_upcard) == "Y"
            if rank == "2":
                assert strategy_pair_splitting(hand_6s, dealer_upcard, das=True) == "Y"
                assert strategy_pair_splitting(hand_6s, dealer_upcard, das=False) == "N"
            else:
                assert strategy_pair_splitting(hand_6s, dealer_upcard, das=True) == "Y"
            if rank in ["2", "3"]:
                assert strategy_pair_splitting(hand_3s, dealer_upcard, das=True) == "Y"
                assert strategy_pair_splitting(hand_3s, dealer_upcard, das=False) == "N"
                assert strategy_pair_splitting(hand_2s, dealer_upcard, das=True) == "Y"
                assert strategy_pair_splitting(hand_2s, dealer_upcard, das=False) == "N"
            else:
                assert strategy_pair_splitting(hand_3s, dealer_upcard) == "Y"
                assert strategy_pair_splitting(hand_2s, dealer_upcard) == "Y"
            if rank in ["2", "3", "4"]:
                assert strategy_pair_splitting(hand_4s, dealer_upcard) == "N"
            else:
                assert strategy_pair_splitting(hand_4s, dealer_upcard, das=True) == "Y"
                assert strategy_pair_splitting(hand_4s, dealer_upcard, das=False) == "N"
        elif rank == "7":
            assert strategy_pair_splitting(hand_9s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_7s, dealer_upcard) == "Y"
            assert strategy_pair_splitting(hand_6s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_4s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_3s, dealer_upcard) == "Y"
            assert strategy_pair_splitting(hand_2s, dealer_upcard) == "Y"
        elif rank in ["8", "9"]:
            assert strategy_pair_splitting(hand_9s, dealer_upcard) == "Y"
            assert strategy_pair_splitting(hand_7s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_6s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_4s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_3s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_2s, dealer_upcard) == "N"
        else:
            assert strategy_pair_splitting(hand_9s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_7s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_6s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_4s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_3s, dealer_upcard) == "N"
            assert strategy_pair_splitting(hand_2s, dealer_upcard) == "N"


def test_soft_totals():
    # No Ace
    hand_noace = Hand(Card("2", "H"), Card("2", "D"))
    with raises(ValueError):
        strategy_soft_totals(hand_noace, Card("A", "H"))

    # Ace
    ace_2 = Hand(Card("A", "H"), Card("2", "H"))
    ace_3 = Hand(Card("A", "H"), Card("3", "H"))
    ace_4 = Hand(Card("A", "H"), Card("4", "H"))
    ace_5 = Hand(Card("A", "H"), Card("5", "H"))
    ace_6 = Hand(Card("A", "H"), Card("6", "H"))
    ace_7 = Hand(Card("A", "H"), Card("7", "H"))
    ace_8 = Hand(Card("A", "H"), Card("8", "H"))
    ace_9 = Hand(Card("A", "H"), Card("9", "H"))
    bj = Hand(Card("A", "H"), Card("K", "H"))

    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        assert strategy(ace_9, dealer_upcard) == "S"
        assert strategy(bj, dealer_upcard) == "S"

        # A,8
        if dealer_upcard.value != 6:
            assert strategy(ace_8, dealer_upcard) == "S"
        else:
            assert strategy(ace_8, dealer_upcard, double=True) == "D"
            assert strategy(ace_8, dealer_upcard, double=False) == "S"

        # A,7
        if dealer_upcard.value <= 6:
            assert strategy(ace_7, dealer_upcard, double=True) == "D"
            assert strategy(ace_7, dealer_upcard, double=False) == "S"
        elif dealer_upcard.value in [7, 8]:
            assert strategy(ace_7, dealer_upcard) == "S"
        else:
            assert strategy(ace_7, dealer_upcard) == "H"

        # A,6
        if 3 <= dealer_upcard.value <= 6:
            assert strategy(ace_6, dealer_upcard, double=True) == "D"
            assert strategy(ace_6, dealer_upcard, double=False) == "H"

        # A,5 / A,4
        if 4 <= dealer_upcard.value <= 6:
            assert strategy(ace_5, dealer_upcard, double=True) == "D"
            assert strategy(ace_5, dealer_upcard, double=False) == "H"
            assert strategy(ace_4, dealer_upcard, double=True) == "D"
            assert strategy(ace_4, dealer_upcard, double=False) == "H"

        # A,3 / A,2
        if 5 <= dealer_upcard.value <= 6:
            assert strategy(ace_3, dealer_upcard, double=True) == "D"
            assert strategy(ace_3, dealer_upcard, double=False) == "H"
            assert strategy(ace_2, dealer_upcard, double=True) == "D"
            assert strategy(ace_2, dealer_upcard, double=False) == "H"


def test_hard_totals():
    hand_21 = Hand(Card("A", "H"), Card("K", "H"))
    hand_20 = Hand(Card("Q", "H"), Card("K", "H"))
    hand_19 = Hand(Card("9", "H"), Card("K", "H"))
    hand_18 = Hand(Card("8", "H"), Card("K", "H"))
    hand_17 = Hand(Card("7", "H"), Card("K", "H"))
    hand_16 = Hand(Card("6", "H"), Card("K", "H"))
    hand_15 = Hand(Card("5", "H"), Card("K", "H"))
    hand_14 = Hand(Card("4", "H"), Card("K", "H"))
    hand_13 = Hand(Card("3", "H"), Card("K", "H"))
    hand_12 = Hand(Card("2", "H"), Card("K", "H"))
    hand_11 = Hand(Card("7", "H"), Card("4", "H"))
    hand_10 = Hand(Card("6", "H"), Card("4", "H"))
    hand_9 = Hand(Card("5", "H"), Card("4", "H"))
    hand_8 = Hand(Card("5", "H"), Card("3", "H"))
    hand_7 = Hand(Card("5", "H"), Card("2", "H"))
    hand_6 = Hand(Card("4", "H"), Card("2", "H"))
    hand_5 = Hand(Card("3", "H"), Card("2", "H"))

    for rank in Ranks:
        dealer_upcard = Card(rank, "H")

        assert strategy(hand_21, dealer_upcard) == "S"
        assert strategy(hand_20, dealer_upcard) == "S"
        assert strategy(hand_19, dealer_upcard) == "S"
        assert strategy(hand_18, dealer_upcard) == "S"
        assert strategy(hand_17, dealer_upcard) == "S"
        assert strategy(hand_11, dealer_upcard, double=True) == "D"
        assert strategy(hand_11, dealer_upcard, double=False) == "H"
        assert strategy(hand_8, dealer_upcard) == "H"
        assert strategy(hand_7, dealer_upcard) == "H"
        assert strategy(hand_6, dealer_upcard) == "H"
        assert strategy(hand_5, dealer_upcard) == "H"

        # 13 - 14 - 15 - 16
        if dealer_upcard.value <= 6:
            assert strategy(hand_16, dealer_upcard) == "S"
            assert strategy(hand_15, dealer_upcard) == "S"
            assert strategy(hand_14, dealer_upcard) == "S"
            assert strategy(hand_13, dealer_upcard) == "S"
        else:
            assert strategy(hand_16, dealer_upcard) == "H"
            assert strategy(hand_15, dealer_upcard) == "H"
            assert strategy(hand_14, dealer_upcard) == "H"
            assert strategy(hand_13, dealer_upcard) == "H"

        # 12
        if dealer_upcard.value <= 3:
            assert strategy(hand_12, dealer_upcard) == "H"
        elif 4 <= dealer_upcard.value <= 6:
            assert strategy(hand_12, dealer_upcard) == "S"
        else:
            assert strategy(hand_12, dealer_upcard) == "H"

        # 10
        if dealer_upcard.value <= 9:
            assert strategy(hand_10, dealer_upcard, double=True) == "D"
            assert strategy(hand_10, dealer_upcard, double=False) == "H"
        else:
            assert strategy(hand_10, dealer_upcard) == "H"

        # 9
        if dealer_upcard.value == 2:
            assert strategy(hand_9, dealer_upcard) == "H"
        elif 3 <= dealer_upcard.value <= 6:
            assert strategy(hand_9, dealer_upcard, double=True) == "D"
            assert strategy(hand_9, dealer_upcard, double=False) == "H"
        else:
            assert strategy(hand_9, dealer_upcard) == "H"


def test_late_surrender():
    hand_14 = Hand(Card("K", "H"), Card("2", "H"), Card("2", "D"))
    hand_15 = Hand(Card("K", "H"), Card("2", "H"), Card("3", "H"))
    hand_16 = Hand(Card("K", "H"), Card("2", "H"), Card("4", "H"))

    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if 9 <= dealer_upcard.value <= 11:
            assert strategy_late_surrender(hand_16, dealer_upcard) is True
            if dealer_upcard.value == 10:
                assert strategy_late_surrender(hand_15, dealer_upcard) is True
                assert strategy_late_surrender(hand_14, dealer_upcard) is False
        else:
            assert strategy_late_surrender(hand_16, dealer_upcard) is False
            assert strategy_late_surrender(hand_15, dealer_upcard) is False
            assert strategy_late_surrender(hand_14, dealer_upcard) is False
