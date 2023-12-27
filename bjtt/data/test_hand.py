from card import Card
from hand import Hand


def test_hand():
    hand = Hand(Card("2", "H"), Card("K", "H"))
    assert hand.cards == [Card("2", "H"), Card("K", "H")]
    assert hand.value == 12
    assert hand.split_available is False
    hand = Hand(Card("2", "H"), Card("2", "C"))
    assert hand.split_available is True


def test_add_card_to_hand():
    hand = Hand(Card("2", "H"), Card("K", "H"))
    hand.add_card(Card("J", "D"))
    assert hand.cards == [Card("2", "H"), Card("K", "H"), Card("J", "D")]
    assert hand.value == 22


def test_hands_comparison():
    hand = Hand(Card("2", "H"), Card("K", "H"))
    inferior_hand = Hand(Card("3", "S"), Card("4", "C"))
    equal_hand = Hand(Card("2", "C"), Card("J", "C"))
    superior_hand = Hand(Card("A", "H"), Card("K", "H"))
    assert hand.value > inferior_hand.value
    assert hand == equal_hand
    assert hand.value < superior_hand.value
