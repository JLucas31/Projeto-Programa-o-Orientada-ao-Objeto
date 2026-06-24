from src.entidade import Entidade


class Artista(Entidade):

    def __init__(
        self,
        id_: str,
        nome: str,
        genero: str,
        pais: str,
        seguidores: int = 0,
        debut_year: int | None = None
    ):
        super().__init__(id_)

        self.__nome = nome
        self.__genero = genero
        self.__pais = pais
        self.__seguidores = seguidores
        self.__debut_year = debut_year

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def genero(self) -> str:
        return self.__genero

    @property
    def pais(self) -> str:
        return self.__pais

    @property
    def seguidores(self) -> int:
        return self.__seguidores

    def adicionar_seguidor(self) -> None:
        self.__seguidores += 1

    def remover_seguidor(self) -> None:
        if self.__seguidores > 0:
            self.__seguidores -= 1

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.__nome,
            "genero": self.__genero,
            "pais": self.__pais,
            "seguidores": self.__seguidores,
            "debut_year": self.__debut_year
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(
            dados["id"],
            dados["nome"],
            dados["genero"],
            dados["pais"],
            dados["seguidores"],
            dados["debut_year"]
        )

    def __str__(self) -> str:
        return f"{self.__nome} ({self.__pais})"