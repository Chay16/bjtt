from typing import List, Type

from card import Card


class Hand:
    def __init__(self, *cards: Type[Card]) -> None:
        self.cards: List[Card] = [card for card in cards]
        self.value: int = sum([card.value for card in self.cards])
        self.split_available: bool = self.cards[0].rank == self.cards[1].rank

    def __eq__(self, other_hand) -> bool:
        return self.value == other_hand.value

    def add_card(self, new_card: Type[Card]) -> None:
        self.cards.append(new_card)
        self.value += new_card.value
