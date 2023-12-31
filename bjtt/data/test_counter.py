from pytest import approx

from .card import Card
from .counter import Counter


def test_counter():
    counter = Counter()
    assert counter.count == 0
    assert counter.true_count == 0
    assert counter.n_decks == 4
    counter.update(Card("A", "H"))
    assert counter.count == -1
    assert counter.true_count == approx(-0.2512, 1e-4)
    counter.update(Card("2", "H"))
    assert counter.count == 0
    assert counter.true_count == approx(0, 1e-4)
    counter.update(Card("3", "H"))
    counter.update(Card("4", "H"))
    counter.update(Card("5", "H"))
    counter.update(Card("6", "H"))
    assert counter.count == 4
    assert counter.true_count == approx(1.0297, 1e-4)
    counter.reset()
    assert counter.count == 0
    assert counter.true_count == 0
    counter.update(Card("7", "H"))
    counter.update(Card("8", "H"))
    assert counter.count == 0
    assert counter.true_count == 0
    counter.update(Card("A", "H"))
    counter.update(Card("J", "H"))
    counter.update(Card("Q", "H"))
    counter.update(Card("K", "H"))
    assert counter.count == -4
    assert counter.true_count == approx(-1.0196, 1e-4)
