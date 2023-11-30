from .interfaces import IHabilidade


class LutaArco(IHabilidade):
    def __init__(self, nivel):
        self.__nivel = nivel

    def comportamento(self):
        print("Atirar flechas")

    def nivel_atributo(self):
        print(f"Nivel de uso arco: {self.__nivel}")
