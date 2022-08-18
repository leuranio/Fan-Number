from game.input import enter
from game.utils import clear_terminal

from .player import Data


def started() -> None:
    clear_terminal()
    print("""
          O jogo começou!
          """)
    enter()


def rules() -> None:
    clear_terminal()
    print("""
          """)
    enter()


def go(nickname: str) -> None:
    clear_terminal()
    print("""
          """)
    enter()


def defeat() -> None:
    clear_terminal()
    print("""
          """)


def try_again() -> None:
    clear_terminal()
    print("""
          Use apenas números, tente novamente!
          """)


def level_zero() -> None:
    clear_terminal()
    print("""
          Você voltou para o level zero, ou quem sabe, talvez você
          nunca tenha passado dele!
          """)


def try_to_guess() -> None:
    print("""
          """)


def congrats() -> None:
    print("""
          """)


def resume(player_data: Data, chance: int, level: int) -> None:
    print("""
          """)
