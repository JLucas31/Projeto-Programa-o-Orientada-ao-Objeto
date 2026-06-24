from src.entidade import Entidade
from src.artista import Artista


class Musica(Entidade):

    def __init__(
        self,
        id_: str,
        titulo: str,
        artista: Artista,
        genero: str,
        duracao_segundos: int,
        formato_audio: str
    ):
        super().__init__(id_)

        self.__titulo = titulo
        self.__artista = artista
        self.__genero = genero
        self.__duracao_segundos = duracao_segundos
        self.__formato_audio = formato_audio

        self.__reproducoes = 0
        self.__curtidas = 0

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def artista(self) -> Artista:
        return self.__artista

    @property
    def genero(self) -> str:
        return self.__genero

    @property
    def duracao_segundos(self) -> int:
        return self.__duracao_segundos

    @property
    def formato_audio(self) -> str:
        return self.__formato_audio

    @property
    def reproducoes(self) -> int:
        return self.__reproducoes

    @property
    def curtidas(self) -> int:
        return self.__curtidas

    def reproduzir(self) -> None:
        self.__reproducoes += 1

    def curtir(self) -> None:
        self.__curtidas += 1

    def alterar_formato(self, novo_formato: str) -> None:
        self.__formato_audio = novo_formato

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "titulo": self.__titulo,
            "artista_id": self.__artista.id,
            "genero": self.__genero,
            "duracao_segundos": self.__duracao_segundos,
            "formato_audio": self.__formato_audio,
            "reproducoes": self.__reproducoes,
            "curtidas": self.__curtidas
        }

    @classmethod
    def from_dict(cls, dados: dict, artista: Artista):
        musica = cls(
            dados["id"],
            dados["titulo"],
            artista,
            dados["genero"],
            dados["duracao_segundos"],
            dados["formato_audio"]
        )

        musica._Musica__reproducoes = dados.get("reproducoes", 0)
        musica._Musica__curtidas = dados.get("curtidas", 0)

        return musica

    def __str__(self) -> str:
        return f"{self.__titulo} - {self.__artista.nome}"