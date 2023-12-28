from pytest import raises

from .card import Card


def test_card():
    card = Card("10", "D")
    assert card.rank == "10"
    assert card.suit == "D"
    assert str(card) == "10 of Diamonds"
    assert repr(card) == "Card('10', 'D')"
    assert card == Card("10", "D")
    assert card != Card("2", "D")
    assert card != Card("10", "H")
    assert card != Card("2", "H")


def test_invalid_card():
    with raises(ValueError):
        Card(1, "H")

    with raises(ValueError):
        Card("10", "Hearts")


def test_card_value():
    assert Card("2", "H").value == 2
    assert Card("J", "H").value == 10
    assert Card("A", "H").value == 11
