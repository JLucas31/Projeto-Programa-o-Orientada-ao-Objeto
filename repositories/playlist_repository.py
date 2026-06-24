from repositories.json_manager import JsonManager
from src.playlist import Playlist


class PlaylistRepository:

    def __init__(
        self,
        usuario_repository,
        musica_repository,
        caminho="database/playlists.json"
    ):

        self.__caminho = caminho

        self.__usuario_repository = (
            usuario_repository
        )

        self.__musica_repository = (
            musica_repository
        )

    def salvar(
        self,
        playlist: Playlist
    ):

        playlists = JsonManager.carregar(
            self.__caminho
        )

        for p in playlists:

            if p["id"] == playlist.id:
                raise ValueError(
                    "Playlist já existe."
                )

        playlists.append(
            playlist.to_dict()
        )

        JsonManager.salvar(
            self.__caminho,
            playlists
        )

    def listar(self):

        dados = JsonManager.carregar(
            self.__caminho
        )

        playlists = []

        for d in dados:

            criador = (
                self.__usuario_repository
                .buscar_por_id(
                    d["criador_id"]
                )
            )

            musicas = []

            for musica_id in d["musicas"]:

                musica = (
                    self.__musica_repository
                    .buscar_por_id(
                        musica_id
                    )
                )

                if musica:
                    musicas.append(
                        musica
                    )

            playlists.append(
                Playlist.from_dict(
                    d,
                    criador,
                    musicas
                )
            )

        return playlists

    def buscar_por_id(
        self,
        id_playlist: str
    ):

        for playlist in self.listar():

            if playlist.id == id_playlist:
                return playlist

        return None

    def remover(
        self,
        id_playlist: str
    ):

        playlists = JsonManager.carregar(
            self.__caminho
        )

        playlists = [
            p
            for p in playlists
            if p["id"] != id_playlist
        ]

        JsonManager.salvar(
            self.__caminho,
            playlists
        )