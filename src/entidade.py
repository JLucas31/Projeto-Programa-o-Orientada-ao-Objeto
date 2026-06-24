from abc import ABC, abstractmethod

class Entidade(ABC):

    def __init__(self, id_: str):
        self._id = id_

    @property
    def id(self) -> str:
        return self._id

    @abstractmethod
    def to_dict(self) -> dict:
        pass