from .habilidades import IHabilidade


class Guerreiro:
    def __init__(self, habilidade: IHabilidade):
        self.__habilidade = habilidade

    def acao(self):
        self.__habilidade.comportamento()

    def atributos(self):
        self.__habilidade.nivel_atributo()
