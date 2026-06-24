from src.entidade import Entidade
from src.musica import Musica
from src.usuario import Usuario


class Playlist(Entidade):

    def __init__(
        self,
        id_: str,
        nome: str,
        criador: Usuario
    ):
        super().__init__(id_)

        self.__nome = nome
        self.__criador = criador
        self.__musicas = []

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def criador(self) -> Usuario:
        return self.__criador

    def adicionar_musica(self, musica: Musica) -> None:

        if musica not in self.__musicas:
            self.__musicas.append(musica)

    def remover_musica(self, musica: Musica) -> None:

        if musica in self.__musicas:
            self.__musicas.remove(musica)

    def listar_musicas(self):
        return self.__musicas.copy()

    def quantidade_musicas(self) -> int:
        return len(self.__musicas)

    def calcular_duracao(self) -> int:

        return sum(
            musica.duracao_segundos
            for musica in self.__musicas
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.__nome,
            "criador_id": self.__criador.id,
            "musicas": [
                musica.id
                for musica in self.__musicas
            ]
        }

    @classmethod
    def from_dict(
        cls,
        dados: dict,
        criador: Usuario,
        musicas: list[Musica]
    ):
        playlist = cls(
            dados["id"],
            dados["nome"],
            criador
        )

        for musica in musicas:
            playlist.adicionar_musica(musica)

        return playlist

    def __str__(self) -> str:
        return f"{self.__nome} ({len(self.__musicas)} músicas)"