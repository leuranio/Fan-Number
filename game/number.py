import random


class RandomNumber:

    def __init__(self, max: int) -> None:
        self.max = max
        self.number = self.__generate()

    def regenerate(self) -> None:
        self.number = self.__generate()

    def __generate(self) -> int:
        return random.randint(0, self.max)
