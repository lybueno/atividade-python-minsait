from serVivo import SerVivo
from personagem import Personagem
from monstro import Monstro
from lobo import Lobo
from goblin import Goblin



humano = Personagem(pontos_de_vida=30, pontos_de_ataque=10, nome="Sir Python")
lobo = Lobo(prontos_de_vida=30, pontos_de_ataque=8, tipo="fera", forca=50)
goblin = Goblin(prontos_de_vida=30, pontos_de_ataque=5, tipo="fera", inteligencia=50)

humano.atacar(goblin)
humano.atacar(goblin)
humano.atacar(goblin)
humano.atacar(goblin)
print(goblin)