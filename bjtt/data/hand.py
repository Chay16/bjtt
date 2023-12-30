from typing import List

from .card import Card


class Hand:
    def __init__(self, *cards: Card) -> None:
        self.cards: List[Card] = [card for card in cards]
        self.soft: bool = False
        self.value: int = 0
        self.compute_value()
        self.split_available: bool = self.cards[0].rank == self.cards[1].rank

    def __str__(self) -> str:
        return f"Hand : {' & '.join([str(card) for card in self.cards])}"

    def __eq__(self, other_hand) -> bool:
        return self.value == other_hand.value

    def compute_value(self) -> None:
        self.soft = False
        self.value = 0
        n_aces = [c.rank for c in self.cards].count("A")
        for card in self.cards:
            if card.rank != "A":
                self.value += card.value
        for i in range(n_aces):
            if self.value <= 10:
                self.soft = True
                self.value += 11
            else:
                self.value += 1

    def add_card(self, new_card: Card) -> None:
        self.cards.append(new_card)
        self.compute_value()
