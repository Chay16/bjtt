from .card import Card
from .hand import Hand


def test_hand():
    hand = Hand(Card("2", "H"), Card("K", "H"))
    assert hand.cards == [Card("2", "H"), Card("K", "H")]
    assert hand.value == 12
    assert hand.split_available is False
    assert str(hand) == "Hand : 2 of Hearts & K of Hearts"
    hand = Hand(Card("2", "H"), Card("2", "C"))
    assert hand.split_available is True
    hand = Hand(Card("A", "H"), Card("K", "H"))
    assert hand.value == 21
    hand = Hand(Card("A", "H"), Card("2", "H"))
    assert hand.value == 13
    hand = Hand(Card("A", "H"), Card("2", "H"), Card("A", "D"))
    assert hand.value == 14


def test_compute_value():
    hand_14 = Hand(Card("A", "H"), Card("3", "H"))
    assert hand_14.value == 14 and hand_14.soft is True
    hand_14 = Hand(Card("K", "H"), Card("4", "H"))
    assert hand_14.value == 14 and hand_14.soft is False
    hand_15 = Hand(Card("A", "H"), Card("A", "D"), Card("3", "H"))
    assert hand_15.value == 15 and hand_15.soft is True
    hand_16 = Hand(Card("A", "H"), Card("2", "D"), Card("3", "H"))
    assert hand_16.value == 16 and hand_16.soft is True
    hand_12 = Hand(Card("A", "H"), Card("9", "D"), Card("2", "H"))
    assert hand_12.value == 12 and hand_12.soft is False

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
