class Data:

    DEFAULT_CHANCE = 10

    def __init__(
        self, victory: int, defeat: int
    ) -> None:
        self.chance: int = self.DEFAULT_CHANCE
        self.victory: int = victory
        self.defeat: int = defeat

    @classmethod
    def emptyData(cls):
        return Data(0, 0)


class Player:

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        self.__player_data = Data.emptyData()

    def get_all_player_data(self) -> Data:
        return self.__player_data
