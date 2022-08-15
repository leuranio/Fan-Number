import input
import message
from player import Player


def mainloop():
    ...


if __name__ == "__main__":
    message.started()
    message.rules()

    nickname = input.typing()
    player = Player(nickname)
