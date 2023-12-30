from .card import Card


class Counter:
    def __init__(self, n_decks: int = 4) -> None:
        self.count: int = 0
        self.running_divisor: float = 0
        self.true_count: float = 0
        self.n_decks: int = n_decks

    def reset(self) -> None:
        self.count = 0
        self.true_count = 0

    def update_count(self, card: Card) -> None:
        if card.value <= 6:
            self.count += 1
        elif 7 <= card.value <= 9:
            self.count += 0
        else:
            self.count -= 1

    def update_running_divisor(self, n_cards: int) -> None:
        self.running_divisor = (52 * self.n_decks - n_cards) / 52

    def update(self, card: Card, n_cards: int) -> None:
        self.update_count(card)
        self.update_running_divisor(n_cards)
        self.true_count = self.count / self.running_divisor
