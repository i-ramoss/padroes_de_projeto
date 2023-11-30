from abc import ABC, abstractmethod


class IHabilidade(ABC):
    @abstractmethod
    def comportamento(self):
        raise NotImplementedError

    @abstractmethod
    def nivel_atributo(self):
        raise NotImplementedError
