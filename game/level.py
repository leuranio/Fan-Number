class NoPreviousLevel(Exception):
    ...


class Level:

    def __init__(self) -> None:
        self.__level = 0

    def next_level(self) -> None:
        self.__level += 1

    def previous_level(self) -> None:
        if self.__level <= 0:
            raise NoPreviousLevel

        self.__level -= 1

    def show_level(self) -> int:
        return self.__level
