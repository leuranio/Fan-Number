from dataclasses import dataclass


class Player:

    def __init__(self, name: str) -> None:
        self.name = name

    @dataclass
    class Data:
        victory: int
        defeat: int

        def ratio(self) -> float:
            total = self.victory + self.defeat
            return total / 2
