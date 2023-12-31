from data.card import Card, Ranks
from data.counter import Counter
from data.hand import Hand
from pytest import raises
from strategy import (
    strategy,
    strategy_late_surrender,
    strategy_pair_splitting,
    strategy_soft_totals,
)


def test_pair_splitting():
    counter_any = Counter()

    # No Split
    hand_nosplit = Hand(Card("A", "H"), Card("2", "D"))
    with raises(ValueError):
        strategy_pair_splitting(hand_nosplit, Card("A", "H"), counter_any)

    # Split
    hand_aces = Hand(Card("A", "H"), Card("A", "D"))
    hand_head = Hand(Card("K", "H"), Card("K", "D"))
    hand_10s = Hand(Card("10", "H"), Card("10", "D"))
    hand_9s = Hand(Card("9", "H"), Card("9", "D"))
    hand_8s = Hand(Card("8", "H"), Card("8", "D"))
    hand_7s = Hand(Card("7", "H"), Card("7", "D"))
    hand_6s = Hand(Card("6", "H"), Card("6", "D"))
    hand_5s = Hand(Card("5", "H"), Card("5", "D"))
    hand_4s = Hand(Card("4", "H"), Card("4", "D"))
    hand_3s = Hand(Card("3", "H"), Card("3", "D"))
    hand_2s = Hand(Card("2", "H"), Card("2", "D"))

    # Aces
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        assert strategy_pair_splitting(hand_aces, dealer_upcard, counter_any) is True

    # Head & 10s
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value == 4:
            count_below_6, count_above_6, count_6 = Counter(), Counter(), Counter()
            count_below_6.true_count = 3
            count_above_6.true_count = 8
            count_6.true_count = 6
            assert (
                strategy_pair_splitting(hand_head, dealer_upcard, count_below_6)
                is False
            )
            assert (
                strategy_pair_splitting(hand_head, dealer_upcard, count_above_6) is True
            )
            assert strategy_pair_splitting(hand_head, dealer_upcard, count_6) is True
            assert (
                strategy_pair_splitting(hand_10s, dealer_upcard, count_below_6) is False
            )
            assert (
                strategy_pair_splitting(hand_10s, dealer_upcard, count_above_6) is True
            )
            assert strategy_pair_splitting(hand_10s, dealer_upcard, count_6) is True
        elif dealer_upcard.value == 5:
            count_below_5, count_above_5, count_5 = Counter(), Counter(), Counter()
            count_below_5.true_count = 3
            count_above_5.true_count = 8
            count_5.true_count = 5
            assert (
                strategy_pair_splitting(hand_head, dealer_upcard, count_below_5)
                is False
            )
            assert (
                strategy_pair_splitting(hand_head, dealer_upcard, count_above_5) is True
            )
            assert strategy_pair_splitting(hand_head, dealer_upcard, count_5) is True
            assert (
                strategy_pair_splitting(hand_10s, dealer_upcard, count_below_5) is False
            )
            assert (
                strategy_pair_splitting(hand_10s, dealer_upcard, count_above_5) is True
            )
            assert strategy_pair_splitting(hand_10s, dealer_upcard, count_5) is True
        elif dealer_upcard.value == 6:
            count_below_4, count_above_4, count_4 = Counter(), Counter(), Counter()
            count_below_4.true_count = 3
            count_above_4.true_count = 8
            count_4.true_count = 4
            assert (
                strategy_pair_splitting(hand_head, dealer_upcard, count_below_4)
                is False
            )
            assert (
                strategy_pair_splitting(hand_head, dealer_upcard, count_above_4) is True
            )
            assert strategy_pair_splitting(hand_head, dealer_upcard, count_4) is True
            assert (
                strategy_pair_splitting(hand_10s, dealer_upcard, count_below_4) is False
            )
            assert (
                strategy_pair_splitting(hand_10s, dealer_upcard, count_above_4) is True
            )
            assert strategy_pair_splitting(hand_10s, dealer_upcard, count_4) is True
        else:
            assert (
                strategy_pair_splitting(hand_head, dealer_upcard, counter_any) is False
            )
            assert (
                strategy_pair_splitting(hand_10s, dealer_upcard, counter_any) is False
            )

    # 9s
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if 2 <= dealer_upcard.value <= 6 or 8 <= dealer_upcard.value <= 9:
            assert strategy_pair_splitting(hand_9s, dealer_upcard, counter_any) is True
        else:
            assert strategy_pair_splitting(hand_9s, dealer_upcard, counter_any) is False

    # 8s
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        assert strategy_pair_splitting(hand_8s, dealer_upcard, counter_any) is True

    # 7s
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value <= 7:
            assert strategy_pair_splitting(hand_7s, dealer_upcard, counter_any) is True
        else:
            assert strategy_pair_splitting(hand_7s, dealer_upcard, counter_any) is False

    # 6s
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value == 2:
            assert (
                strategy_pair_splitting(hand_6s, dealer_upcard, counter_any, das=True)
                is True
            )
            assert (
                strategy_pair_splitting(hand_6s, dealer_upcard, counter_any, das=False)
                is False
            )
        elif 3 <= dealer_upcard.value <= 6:
            assert strategy_pair_splitting(hand_6s, dealer_upcard, counter_any) is True
        else:
            assert strategy_pair_splitting(hand_6s, dealer_upcard, counter_any) is False

    # 5s
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        assert strategy_pair_splitting(hand_5s, dealer_upcard, counter_any) is False

    # 4s
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if 5 <= dealer_upcard.value <= 6:
            assert (
                strategy_pair_splitting(hand_4s, dealer_upcard, counter_any, das=True)
                is True
            )
            assert (
                strategy_pair_splitting(hand_4s, dealer_upcard, counter_any, das=False)
                is False
            )
        else:
            assert strategy_pair_splitting(hand_4s, dealer_upcard, counter_any) is False

    # 3s & 2s
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if 2 <= dealer_upcard.value <= 3:
            assert (
                strategy_pair_splitting(hand_3s, dealer_upcard, counter_any, das=True)
                is True
            )
            assert (
                strategy_pair_splitting(hand_3s, dealer_upcard, counter_any, das=False)
                is False
            )
            assert (
                strategy_pair_splitting(hand_2s, dealer_upcard, counter_any, das=True)
                is True
            )
            assert (
                strategy_pair_splitting(hand_2s, dealer_upcard, counter_any, das=False)
                is False
            )
        elif 4 <= dealer_upcard.value <= 7:
            assert strategy_pair_splitting(hand_3s, dealer_upcard, counter_any) is True
            assert strategy_pair_splitting(hand_2s, dealer_upcard, counter_any) is True
        else:
            assert strategy_pair_splitting(hand_3s, dealer_upcard, counter_any) is False
            assert strategy_pair_splitting(hand_2s, dealer_upcard, counter_any) is False


def test_soft_totals():
    counter_any = Counter()

    # No Ace
    hand_noace = Hand(Card("2", "H"), Card("2", "D"))
    with raises(ValueError):
        strategy_soft_totals(hand_noace, Card("A", "H"), counter_any)

    # Hands
    ace_2 = Hand(Card("A", "H"), Card("2", "H"))
    ace_3 = Hand(Card("A", "H"), Card("3", "H"))
    ace_4 = Hand(Card("A", "H"), Card("4", "H"))
    ace_5 = Hand(Card("A", "H"), Card("5", "H"))
    ace_5_double = Hand(Card("A", "H"), Card("2", "H"), Card("3", "H"))
    ace_6 = Hand(Card("A", "H"), Card("6", "H"))
    ace_7 = Hand(Card("A", "H"), Card("7", "H"))
    ace_8 = Hand(Card("A", "H"), Card("8", "H"))
    ace_9 = Hand(Card("A", "H"), Card("9", "H"))
    bj = Hand(Card("A", "H"), Card("K", "H"))

    # BJ & A,9
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        assert strategy_soft_totals(bj, dealer_upcard, counter_any) == "S"
        assert strategy_soft_totals(ace_9, dealer_upcard, counter_any) == "S"

    # A,8
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value == 4:
            count_below_3, count_above_3, count_3 = Counter(), Counter(), Counter()
            count_below_3.true_count = -2
            count_above_3.true_count = 8
            count_3.true_count = 3
            assert strategy_soft_totals(ace_8, dealer_upcard, count_below_3) == "S"
            assert strategy_soft_totals(ace_8, dealer_upcard, count_3) == "H"
            assert strategy_soft_totals(ace_8, dealer_upcard, count_above_3) == "H"
        elif dealer_upcard.value == 5:
            count_below_1, count_above_1, count_1 = Counter(), Counter(), Counter()
            count_below_1.true_count = -1
            count_above_1.true_count = 8
            count_1.true_count = 1
            assert strategy_soft_totals(ace_8, dealer_upcard, count_below_1) == "S"
            assert strategy_soft_totals(ace_8, dealer_upcard, count_1) == "H"
            assert strategy_soft_totals(ace_8, dealer_upcard, count_above_1) == "H"
        elif dealer_upcard.value == 6:
            count_below_0, count_above_0, count_0 = Counter(), Counter(), Counter()
            count_below_0.true_count = -2
            count_above_0.true_count = 8
            count_0.true_count = 0
            assert strategy_soft_totals(ace_8, dealer_upcard, count_below_0) == "S"
            assert (
                strategy_soft_totals(ace_8, dealer_upcard, count_0, double=True) == "S"
            )
            assert (
                strategy_soft_totals(ace_8, dealer_upcard, count_0, double=False) == "S"
            )
            assert (
                strategy_soft_totals(ace_8, dealer_upcard, count_above_0, double=True)
                == "D"
            )
            assert (
                strategy_soft_totals(ace_8, dealer_upcard, count_above_0, double=False)
                == "S"
            )
        else:
            assert strategy_soft_totals(ace_8, dealer_upcard, counter_any) == "S"

    # A,7
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value <= 6:
            assert (
                strategy_soft_totals(ace_7, dealer_upcard, counter_any, double=True)
                == "D"
            )
            assert (
                strategy_soft_totals(ace_7, dealer_upcard, counter_any, double=False)
                == "S"
            )
        elif 7 <= dealer_upcard.value <= 8:
            assert strategy_soft_totals(ace_7, dealer_upcard, counter_any) == "S"
        else:
            assert strategy_soft_totals(ace_7, dealer_upcard, counter_any) == "H"

    # A,6
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value == 2:
            count_below_1, count_above_1, count_1 = Counter(), Counter(), Counter()
            count_below_1.true_count = -2
            count_above_1.true_count = 8
            count_1.true_count = 1
            assert strategy_soft_totals(ace_6, dealer_upcard, count_below_1) == "H"
            assert strategy_soft_totals(ace_6, dealer_upcard, count_1) == "S"
            assert strategy_soft_totals(ace_6, dealer_upcard, count_above_1) == "S"
        elif 3 <= dealer_upcard.value <= 6:
            assert (
                strategy_soft_totals(ace_6, dealer_upcard, counter_any, double=True)
                == "D"
            )
            assert (
                strategy_soft_totals(ace_6, dealer_upcard, counter_any, double=False)
                == "H"
            )
        else:
            assert strategy_soft_totals(ace_6, dealer_upcard, counter_any) == "H"

    # A,5 & A,4
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if 4 <= dealer_upcard.value <= 6:
            assert (
                strategy_soft_totals(ace_5, dealer_upcard, counter_any, double=True)
                == "D"
            )
            assert (
                strategy_soft_totals(ace_5, dealer_upcard, counter_any, double=False)
                == "H"
            )
            assert (
                strategy_soft_totals(
                    ace_5_double, dealer_upcard, counter_any, double=True
                )
                == "D"
            )
            assert (
                strategy_soft_totals(
                    ace_5_double, dealer_upcard, counter_any, double=False
                )
                == "H"
            )
            assert (
                strategy_soft_totals(ace_4, dealer_upcard, counter_any, double=True)
                == "D"
            )
            assert (
                strategy_soft_totals(ace_4, dealer_upcard, counter_any, double=False)
                == "H"
            )
        else:
            assert strategy_soft_totals(ace_5, dealer_upcard, counter_any) == "H"
            assert strategy_soft_totals(ace_5_double, dealer_upcard, counter_any) == "H"
            assert strategy_soft_totals(ace_4, dealer_upcard, counter_any) == "H"

    # A,3 & A,2
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if 5 <= dealer_upcard.value <= 6:
            assert (
                strategy_soft_totals(ace_3, dealer_upcard, counter_any, double=True)
                == "D"
            )
            assert (
                strategy_soft_totals(ace_3, dealer_upcard, counter_any, double=False)
                == "H"
            )
            assert (
                strategy_soft_totals(ace_2, dealer_upcard, counter_any, double=True)
                == "D"
            )
            assert (
                strategy_soft_totals(ace_2, dealer_upcard, counter_any, double=False)
                == "H"
            )
        else:
            assert strategy_soft_totals(ace_3, dealer_upcard, counter_any) == "H"
            assert strategy_soft_totals(ace_2, dealer_upcard, counter_any) == "H"


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

    counter_any = Counter()

    # 17 - 18 - 19 - 20 - 21
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        assert strategy(hand_21, dealer_upcard, counter_any) == "S"
        assert strategy(hand_20, dealer_upcard, counter_any) == "S"
        assert strategy(hand_19, dealer_upcard, counter_any) == "S"
        assert strategy(hand_18, dealer_upcard, counter_any) == "S"
        assert strategy(hand_17, dealer_upcard, counter_any) == "S"

    # 16
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value <= 6:
            assert strategy(hand_16, dealer_upcard, counter_any) == "S"
        elif 7 <= dealer_upcard.value <= 8:
            assert strategy(hand_16, dealer_upcard, counter_any) == "H"
        elif dealer_upcard.value == 9:
            count_below_4, count_above_4, count_4 = Counter(), Counter(), Counter()
            count_below_4.true_count = -2
            count_above_4.true_count = 8
            count_4.true_count = 4
            assert strategy(hand_16, dealer_upcard, count_below_4) == "H"
            assert strategy(hand_16, dealer_upcard, count_4) == "S"
            assert strategy(hand_16, dealer_upcard, count_above_4) == "S"
        elif dealer_upcard.value == 10:
            count_below_0, count_above_0, count_0 = Counter(), Counter(), Counter()
            count_below_0.true_count = -2
            count_above_0.true_count = 8
            count_0.true_count = 0
            assert strategy(hand_16, dealer_upcard, count_below_0) == "H"
            assert strategy(hand_16, dealer_upcard, count_0) == "S"
            assert strategy(hand_16, dealer_upcard, count_above_0) == "S"
        else:
            count_below_3, count_above_3, count_3 = Counter(), Counter(), Counter()
            count_below_3.true_count = -2
            count_above_3.true_count = 8
            count_3.true_count = 3
            assert strategy(hand_16, dealer_upcard, count_below_3) == "H"
            assert strategy(hand_16, dealer_upcard, count_3) == "S"
            assert strategy(hand_16, dealer_upcard, count_above_3) == "S"

    # 15
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value <= 6:
            assert strategy(hand_16, dealer_upcard, counter_any) == "S"
        elif 7 <= dealer_upcard.value <= 9:
            assert strategy(hand_16, dealer_upcard, counter_any) == "H"
        elif dealer_upcard.value == 10:
            count_below_4, count_above_4, count_4 = Counter(), Counter(), Counter()
            count_below_4.true_count = -2
            count_above_4.true_count = 8
            count_4.true_count = 4
            assert strategy(hand_15, dealer_upcard, count_below_4) == "H"
            assert strategy(hand_15, dealer_upcard, count_4) == "S"
            assert strategy(hand_15, dealer_upcard, count_above_4) == "S"
        else:
            count_below_5, count_above_5, count_5 = Counter(), Counter(), Counter()
            count_below_5.true_count = -2
            count_above_5.true_count = 8
            count_5.true_count = 5
            assert strategy(hand_15, dealer_upcard, count_below_5) == "H"
            assert strategy(hand_15, dealer_upcard, count_5) == "S"
            assert strategy(hand_15, dealer_upcard, count_above_5) == "S"

    # 14
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        print(dealer_upcard)
        if dealer_upcard.value <= 6:
            assert strategy(hand_14, dealer_upcard, counter_any) == "S"
        else:
            assert strategy(hand_14, dealer_upcard, counter_any) == "H"
    # 13
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value == 2:
            count_below_neg_1, count_above_neg_1, count_neg_1 = (
                Counter(),
                Counter(),
                Counter(),
            )
            count_below_neg_1.true_count = -2
            count_above_neg_1.true_count = 8
            count_neg_1.true_count = -1
            assert strategy(hand_13, dealer_upcard, count_below_neg_1) == "H"
            assert strategy(hand_13, dealer_upcard, count_neg_1) == "H"
            assert strategy(hand_13, dealer_upcard, count_above_neg_1) == "S"
        elif 3 <= dealer_upcard.value <= 6:
            assert strategy(hand_13, dealer_upcard, counter_any) == "S"
        else:
            assert strategy(hand_13, dealer_upcard, counter_any) == "H"
    # 12
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value == 2:
            count_below_3, count_above_3, count_3 = Counter(), Counter(), Counter()
            count_below_3.true_count = -2
            count_above_3.true_count = 8
            count_3.true_count = 3
            assert strategy(hand_12, dealer_upcard, count_below_3) == "H"
            assert strategy(hand_12, dealer_upcard, count_3) == "S"
            assert strategy(hand_12, dealer_upcard, count_above_3) == "S"
        elif dealer_upcard.value == 3:
            count_below_2, count_above_2, count_2 = Counter(), Counter(), Counter()
            count_below_2.true_count = -2
            count_above_2.true_count = 8
            count_2.true_count = 2
            assert strategy(hand_12, dealer_upcard, count_below_2) == "H"
            assert strategy(hand_12, dealer_upcard, count_2) == "S"
            assert strategy(hand_12, dealer_upcard, count_above_2) == "S"
        elif dealer_upcard.value == 4:
            count_below_0, count_above_0, count_0 = Counter(), Counter(), Counter()
            count_below_0.true_count = -2
            count_above_0.true_count = 8
            count_0.true_count = 0
            assert strategy(hand_12, dealer_upcard, count_below_0) == "H"
            assert strategy(hand_12, dealer_upcard, count_0) == "H"
            assert strategy(hand_12, dealer_upcard, count_above_0) == "S"
        elif 5 <= dealer_upcard.value <= 6:
            assert strategy(hand_12, dealer_upcard, counter_any) == "S"
        else:
            assert strategy(hand_12, dealer_upcard, counter_any) == "H"
    # 11
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        assert strategy(hand_11, dealer_upcard, counter_any, double=True) == "D"
        assert strategy(hand_11, dealer_upcard, counter_any, double=False) == "H"

    # 10
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value <= 9:
            assert strategy(hand_10, dealer_upcard, counter_any, double=True) == "D"
            assert strategy(hand_10, dealer_upcard, counter_any, double=False) == "H"
        elif dealer_upcard.value == 10:
            count_below_4, count_above_4, count_4 = Counter(), Counter(), Counter()
            count_below_4.true_count = -2
            count_above_4.true_count = 8
            count_4.true_count = 4
            assert strategy(hand_10, dealer_upcard, count_below_4) == "H"
            assert strategy(hand_10, dealer_upcard, count_4) == "S"
            assert strategy(hand_10, dealer_upcard, count_above_4) == "S"
        else:
            count_below_3, count_above_3, count_3 = Counter(), Counter(), Counter()
            count_below_3.true_count = -2
            count_above_3.true_count = 8
            count_3.true_count = 3
            assert strategy(hand_10, dealer_upcard, count_below_3) == "H"
            assert strategy(hand_10, dealer_upcard, count_3) == "S"
            assert strategy(hand_10, dealer_upcard, count_above_3) == "S"

    # 9
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value == 2:
            count_below_1, count_above_1, count_1 = Counter(), Counter(), Counter()
            count_below_1.true_count = -2
            count_above_1.true_count = 8
            count_1.true_count = 1
            assert strategy(hand_8, dealer_upcard, count_below_1) == "H"
            assert strategy(hand_9, dealer_upcard, count_1) == "S"
            assert strategy(hand_9, dealer_upcard, count_above_1) == "S"
        elif 3 <= dealer_upcard.value <= 6:
            assert strategy(hand_9, dealer_upcard, counter_any, double=True) == "D"
            assert strategy(hand_9, dealer_upcard, counter_any, double=False) == "H"
        elif dealer_upcard.value == 7:
            count_below_3, count_above_3, count_3 = Counter(), Counter(), Counter()
            count_below_3.true_count = -2
            count_above_3.true_count = 8
            count_3.true_count = 3
            assert strategy(hand_9, dealer_upcard, count_below_3) == "H"
            assert strategy(hand_9, dealer_upcard, count_3) == "S"
            assert strategy(hand_9, dealer_upcard, count_above_3) == "S"
        else:
            assert strategy(hand_9, dealer_upcard, counter_any) == "H"

    # 8
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value == 6:
            count_below_2, count_above_2, count_2 = Counter(), Counter(), Counter()
            count_below_2.true_count = -2
            count_above_2.true_count = 8
            count_2.true_count = 2
            assert strategy(hand_8, dealer_upcard, count_below_2) == "H"
            assert strategy(hand_8, dealer_upcard, count_2) == "S"
            assert strategy(hand_8, dealer_upcard, count_above_2) == "S"
        else:
            assert strategy(hand_8, dealer_upcard, counter_any) == "H"

    # 7 - 6 - 5
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        assert strategy(hand_7, dealer_upcard, counter_any) == "H"
        assert strategy(hand_6, dealer_upcard, counter_any) == "H"
        assert strategy(hand_5, dealer_upcard, counter_any) == "H"


def test_late_surrender():
    hand_14 = Hand(Card("K", "H"), Card("2", "H"), Card("2", "D"))
    hand_15 = Hand(Card("K", "H"), Card("2", "H"), Card("3", "H"))
    hand_16 = Hand(Card("K", "H"), Card("2", "H"), Card("4", "H"))
    hand_17 = Hand(Card("K", "H"), Card("3", "H"), Card("4", "H"))

    counter_any = Counter()

    # 17
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value == 11:
            assert strategy_late_surrender(hand_17, dealer_upcard, counter_any) is True
        else:
            assert strategy_late_surrender(hand_17, dealer_upcard, counter_any) is False

    # 16
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value <= 7:
            assert strategy_late_surrender(hand_16, dealer_upcard, counter_any) is False
        elif dealer_upcard.value == 8:
            count_below_4, count_above_4, count_4 = Counter(), Counter(), Counter()
            count_below_4.true_count = -2
            count_above_4.true_count = 8
            count_4.true_count = 4
            assert (
                strategy_late_surrender(hand_16, dealer_upcard, count_below_4) is False
            )
            assert strategy_late_surrender(hand_16, dealer_upcard, count_4) is True
            assert (
                strategy_late_surrender(hand_16, dealer_upcard, count_above_4) is True
            )
        elif dealer_upcard.value == 9:
            count_below_neg_1, count_above_neg_1, count_neg_1 = (
                Counter(),
                Counter(),
                Counter(),
            )
            count_below_neg_1.true_count = -2
            count_above_neg_1.true_count = 8
            count_neg_1.true_count = -1
            assert (
                strategy_late_surrender(hand_16, dealer_upcard, count_below_neg_1)
                is False
            )
            assert strategy_late_surrender(hand_16, dealer_upcard, count_neg_1) is False
            assert (
                strategy_late_surrender(hand_16, dealer_upcard, count_above_neg_1)
                is True
            )
        else:
            assert strategy_late_surrender(hand_16, dealer_upcard, counter_any) is True

    # 15
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        if dealer_upcard.value == 9:
            count_below_2, count_above_2, count_2 = Counter(), Counter(), Counter()
            count_below_2.true_count = -2
            count_above_2.true_count = 8
            count_2.true_count = 2
            assert (
                strategy_late_surrender(hand_15, dealer_upcard, count_below_2) is False
            )
            assert strategy_late_surrender(hand_15, dealer_upcard, count_2) is True
            assert (
                strategy_late_surrender(hand_15, dealer_upcard, count_above_2) is True
            )
        elif dealer_upcard.value == 10:
            count_below_0, count_above_0, count_0 = Counter(), Counter(), Counter()
            count_below_0.true_count = -2
            count_above_0.true_count = 8
            count_0.true_count = 0
            assert (
                strategy_late_surrender(hand_15, dealer_upcard, count_below_0) is False
            )
            assert strategy_late_surrender(hand_15, dealer_upcard, count_0) is False
            assert (
                strategy_late_surrender(hand_15, dealer_upcard, count_above_0) is True
            )
        elif dealer_upcard.value == 11:
            count_below_neg_1, count_above_neg_1, count_neg_1 = (
                Counter(),
                Counter(),
                Counter(),
            )
            count_below_neg_1.true_count = -2
            count_above_neg_1.true_count = 8
            count_neg_1.true_count = -1
            assert (
                strategy_late_surrender(hand_15, dealer_upcard, count_below_neg_1)
                is False
            )
            assert strategy_late_surrender(hand_15, dealer_upcard, count_neg_1) is True
            assert (
                strategy_late_surrender(hand_15, dealer_upcard, count_above_neg_1)
                is True
            )
        else:
            assert strategy_late_surrender(hand_15, dealer_upcard, counter_any) is False

    # 14
    for rank in Ranks:
        dealer_upcard = Card(rank, "H")
        assert strategy_late_surrender(hand_14, dealer_upcard, counter_any) is False
