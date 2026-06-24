from src.entidade import Entidade
from src.plano import Plano


class Usuario(Entidade):

    def __init__(
        self,
        id_: str,
        username: str,
        email: str,
        plano: Plano
    ):
        super().__init__(id_)

        if not self.validar_email(email):
            raise ValueError("Email inválido")

        self.__username = username
        self.__email = email
        self.__plano = plano
        self.__playlists = []

    @property
    def username(self) -> str:
        return self.__username

    @property
    def email(self) -> str:
        return self.__email

    @property
    def plano(self) -> Plano:
        return self.__plano

    def criar_playlist(self, playlist) -> None:
        self.__playlists.append(playlist)

    def listar_playlists(self):
        return self.__playlists.copy()

    @staticmethod
    def validar_email(email: str) -> bool:

        if email.count("@") != 1:
            return False

        usuario, dominio = email.split("@")

        if not usuario:
            return False

        if not dominio:
            return False

        if "." not in dominio:
            return False

        return True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.__username,
            "email": self.__email,
            "plano": self.__plano.__class__.__name__
        }

    @classmethod
    def from_dict(cls, dados: dict, plano: Plano):
        return cls(
            dados["id"],
            dados["username"],
            dados["email"],
            plano
        )

    def __str__(self) -> str:
        return self.__username