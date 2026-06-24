from abc import ABC, abstractmethod

class Plano(ABC):

    @abstractmethod
    def limite_downloads(self) -> int:
        pass

    @abstractmethod
    def qualidade_audio(self) -> str:
        pass

    @abstractmethod
    def exibir_beneficios(self) -> list[str]:
        pass