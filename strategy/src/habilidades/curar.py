from .interfaces import IHabilidade


class Curar(IHabilidade):
    def __init__(self, nivel):
        self.__nivel = nivel

    def comportamento(self):
        print("Curar personagem")

    def nivel_atributo(self):
        print(f"Nivel de cura: {self.__nivel}")
