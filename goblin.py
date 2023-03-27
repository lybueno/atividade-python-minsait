from monstro import Monstro

class Goblin(Monstro):

    def __init__(self, pontos_de_vida: int, pontos_de_ataque: int, tipo: str, inteligencia: int):
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.inteligencia: int = inteligencia