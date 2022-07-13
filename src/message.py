from abc import abstractmethod
import os

from player import Player


class Message:
    
    def clear_console(self):
        os.system('cls')
    
    def set_player_nickname(self) -> None:
        self.clear_console()
        print("""
              Ei jogador, defina um nome para você, não é porque o jogo é
              pequeno que você não precisa escolher um digno de ser usado!
              Use sua criatividade!
              """)
        
    def rules(self, game_name: str, nickname: str, total: int, max_chance: int) -> None:
        self.clear_console()
        print("""
              {}, está prestes a começar e você não pode jogar sem sa-
              ber as regras básicas. {}, iremos gerar um número de 0 a 
              {}, e você terá que desvenda-lo, faça 10 pontos e ira para
              o próximo round. A cada round um dígito é adicionado ao ma-
              ximo de números(e.g. 9 -> 99 -> 999 -> etc...)
              
              Você tem {} chances por round, e a cada vitória ganha mais 
              uma ao total.
              """.format(game_name, nickname, total, max_chance))
        Input.enter()
        
    def started(self, nickname: str) -> None:
        self.clear_console()
        print("""
              {}, o jogo começou, vamos gerar um número, tente descobrir,
              qual foi!
              """.format(nickname))
        
    def wrong(self, nickname: str, chance: int) -> None:
        self.clear_console()
        print("""
              {}, tente novamente, agora você tem {} chances!
              """.format(nickname, chance))
    
    def only_number(self, nickname: str) -> None:
        print("""
                Lembrando que o jogo só funciona com números, ou
                será que existe uma letra coringa pra tudo isso?
                
                {}, por agora, tente novamente, nenhuma de suas
                tentativas foi perdita!
                """.format(nickname))
    
    def try_again(self) -> None:
        self.clear_console()
        print("""
              Deseja continuar, ou quer parar por aqui? (s/n)
              """)
        
class Input:

    INPUT_CARRET = '::'

    @abstractmethod
    def player_nickname(player: Player) -> None:
        value = input(Input.INPUT_CARRET)
        player.nickname = value.capitalize()

    @abstractmethod
    def number() -> str:
        return input(Input.INPUT_CARRET)

    @abstractmethod
    def option() -> bool:
        value = input(Input.INPUT_CARRET)
        return True if value == 'y' else False
    
    @abstractmethod
    def enter() -> None:
        input(f'(Enter para continuar){Input.INPUT_CARRET}')
