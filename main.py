from serVivo import SerVivo
from personagem import Personagem
from monstro import Monstro
from lobo import Lobo
from goblin import Goblin



humano = Personagem(30, 10, "Sir Python")
lobo = Lobo(30, 5,"fera", 50)
goblin = Goblin(30, 5,"fera", 50)

humano.atacar(goblin)
humano.atacar(goblin)
humano.atacar(goblin)
humano.atacar(goblin)
print(goblin)