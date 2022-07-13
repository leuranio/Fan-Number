class Player:

    def __init__(self, nickname: str) -> None:
        self.nickname: str = nickname
        self.point: int = 0
        self.victory: int = 0
        self.defeat: int = 0
        self.round: int = 0
        self.chance: int = 12
