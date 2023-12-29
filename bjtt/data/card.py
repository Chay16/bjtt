Ranks = [
    "A",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
]

Suits = ["S", "H", "D", "C"]


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        if rank not in Ranks:
            raise ValueError(f"{rank} is not a valid rank")
        if suit not in Suits:
            raise ValueError(f"{suit} is not a valid suit")
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        suitoString = {"S": "Spades", "H": "Hearts", "D": "Diamonds", "C": "Clubs"}
        return f"{self.rank} of {suitoString[self.suit]}"

    def __repr__(self) -> str:
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other_card) -> bool:
        return (self.rank == other_card.rank) and (self.suit == other_card.suit)

    @property
    def value(self) -> int:
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)
