from abc import abstractmethod
from random import Random
from message import Message, Input
from player import Player


class Game:
    
    def __init__(self) -> None:
        self.player: Player = Player(None)
        self.message: Message = Message()
        self.name: str = 'Random Number'
        
        self.generated = 0
        self.max_chance = 12
        self.total = 9

    def run(self) -> None:
        self.message.set_player_nickname()
        Input.player_nickname(self.player)
        
        self.message.rules(self.name,
                           self.player.nickname,
                           self.total,
                           self.max_chance)
        
        self.mainloop()
        
    def mainloop(self) -> None:
        nickname = self.player.nickname
        self.message.started(nickname)
        self.generate()
        
        chance = self.player.chance
        victory = self.player.victory
        defeat = self.player.defeat
        point = self.player.point
        round = self.player.round
        while self.player.chance >= 0:
            if chance == 0:
                defeat += 1
                point -= 1
                self.next_round()
            else:
                try:
                    number = Input.number()
                    if int(number) == self.generated:
                        self.next_round()
                        victory += 1
                        point += 1
                        round += 1
                    else:
                        self.message.wrong(nickname, chance)
                        chance -= 1

                except ValueError:
                    self.message.only_number(nickname)

    def generate(self) -> None:
        self.generated = Random().randint(0, self.total)
        
    def next_round(self) -> None:
        self.message.try_again()
        option = Input.option()
        if not option:
            return
        
        self.player.chance = self.total
        self.generate()
            

def main() -> None:
    game = Game()
    game.run()

main()
