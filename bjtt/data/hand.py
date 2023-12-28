from typing import List

from .card import Card


class Hand:
    def __init__(self, *cards: Card) -> None:
        self.cards: List[Card] = [card for card in cards]
        self.value: int = 0
        for card in self.cards:
            if card.rank == "A" and self.value >= 11:
                self.value += 1
            else:
                self.value += card.value
        self.split_available: bool = self.cards[0].rank == self.cards[1].rank

    def __str__(self) -> str:
        return f"Hand : {' & '.join([str(card) for card in self.cards])}"

    def __eq__(self, other_hand) -> bool:
        return self.value == other_hand.value

    def add_card(self, new_card: Card) -> None:
        self.cards.append(new_card)
        self.value += new_card.value
