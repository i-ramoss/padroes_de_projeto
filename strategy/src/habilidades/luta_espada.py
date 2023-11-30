from .interfaces import IHabilidade


class LutaEspada(IHabilidade):
    def __init__(self, nivel):
        self.__nivel = nivel

    def comportamento(self):
        print("Lutar com espada")

    def nivel_atributo(self):
        print(f"Nivel de uso espada: {self.__nivel}")
