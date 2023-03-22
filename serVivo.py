from __future__ import annotations  


class SerVivo():

    def __init__(self, pontos_de_vida, pontos_de_ataque):
        self.pontos_de_ataque: int = pontos_de_ataque
        self.pontos_de_vida: int = pontos_de_vida

    def resultado_ataque(self, pontos_de_vida: int, pontos_de_ataque: int):
        print(f'O adversário escolhido recebeu [{pontos_de_ataque}] de dano e agora possui: [{pontos_de_vida}] de vida')

    def atacar(self, criatura: SerVivo):
        if self.validar_ataque(criatura.pontos_de_vida, self.pontos_de_ataque):
            criatura.pontos_de_vida -= self.pontos_de_ataque
            self.resultado_ataque(criatura.pontos_de_vida, self.pontos_de_ataque)
        else:
            criatura.pontos_de_vida = 0
            print('O adversário atacado está morto')

    def validar_ataque(self, pontos_de_vida: int, pontos_de_ataque: int) -> bool:
        return(pontos_de_vida > pontos_de_ataque)
            
    def __str__(self) -> str:
        class_name = self.__class__.__name__
        attr = f'(PV: {self.pontos_de_vida} PA: {self.pontos_de_ataque})'
        return class_name + attr