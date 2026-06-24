from repositories.json_manager import JsonManager
from src.musica import Musica


class MusicaRepository:

    def __init__(
        self,
        artista_repository,
        caminho="database/musicas.json"
    ):

        self.__caminho = caminho
        self.__artista_repository = (
            artista_repository
        )

    def salvar(
        self,
        musica: Musica
    ):

        musicas = JsonManager.carregar(
            self.__caminho
        )

        for m in musicas:

            if m["id"] == musica.id:
                raise ValueError(
                    "Música já cadastrada."
                )

        musicas.append(
            musica.to_dict()
        )

        JsonManager.salvar(
            self.__caminho,
            musicas
        )

    def listar(self):

        dados = JsonManager.carregar(
            self.__caminho
        )

        musicas = []

        for d in dados:

            artista = (
                self.__artista_repository
                .buscar_por_id(
                    d["artista_id"]
                )
            )

            musicas.append(
                Musica.from_dict(
                    d,
                    artista
                )
            )

        return musicas

    def buscar_por_id(
        self,
        id_musica: str
    ):

        for musica in self.listar():

            if musica.id == id_musica:
                return musica

        return None

    def remover(
        self,
        id_musica: str
    ):

        musicas = JsonManager.carregar(
            self.__caminho
        )

        musicas = [
            m
            for m in musicas
            if m["id"] != id_musica
        ]

        JsonManager.salvar(
            self.__caminho,
            musicas
        )