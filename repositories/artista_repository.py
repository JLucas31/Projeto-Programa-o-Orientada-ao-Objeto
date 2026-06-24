from repositories.json_manager import JsonManager
from src.artista import Artista


class ArtistaRepository:

    def __init__(
        self,
        caminho="database/artistas.json"
    ):
        self.__caminho = caminho

    def salvar(self, artista: Artista):

        artistas = JsonManager.carregar(
            self.__caminho
        )

        for a in artistas:

            if a["id"] == artista.id:
                raise ValueError(
                    "Artista já cadastrado."
                )

        artistas.append(
            artista.to_dict()
        )

        JsonManager.salvar(
            self.__caminho,
            artistas
        )

    def listar(self):

        dados = JsonManager.carregar(
            self.__caminho
        )

        return [
            Artista.from_dict(d)
            for d in dados
        ]

    def buscar_por_id(
        self,
        id_artista: str
    ):

        dados = JsonManager.carregar(self.__caminho)

        for artista in dados:

            if artista["id"] == id_artista:
                return Artista.from_dict(artista)

        return None

    def remover(self,id_artista: str):

        artistas = JsonManager.carregar(self.__caminho)

        artistas = [a for a in artistas if a["id"] != id_artista]

        JsonManager.salvar(
            self.__caminho,
            artistas
        )