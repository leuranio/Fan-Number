from game import message
from game.input import OnlyNumber, confirm, digit, typing
from game.level import Level, NoPreviousLevel
from game.number import RandomNumber
from game.player import Data, Player


def mainloop(player: Player):
    player_data: Data = player.get_all_player_data()

    number = RandomNumber(12)
    level = Level()
    chance: int = player_data.chance
    while chance <= 1:
        if chance == 0:
            ...
        else:
            try:
                message.try_to_guess()
                guess = digit()
                if guess == number.number:
                    message.congrats()
                    if confirm():
                        level.next_level()
                        chance = Data.DEFAULT_CHANCE
                        player_data.victory += 1
                    else:
                        message.resume(
                            player_data, chance, level.show_level()
                        )
                        break
                else:
                    level.previous_level()
                    player_data.defeat += 1
                    if confirm():
                        ...
            except OnlyNumber:
                message.try_again()
            except NoPreviousLevel:
                message.level_zero()


if __name__ == "__main__":
    message.started()
    message.rules()

    nickname = typing()

    message.go(nickname)
    mainloop(Player(nickname))
