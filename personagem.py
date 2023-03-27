from serVivo import SerVivo

class Personagem(SerVivo):
    
    def __init__(self, pontos_de_vida: int, pontos_de_ataque: int, nome: str):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.nome:str = nome