from repositories.json_manager import JsonManager
from src.usuario import Usuario
from src.plano_free import PlanoFree
from src.plano_premium import PlanoPremium


class UsuarioRepository:

    def __init__(
        self,
        caminho="database/usuarios.json"
    ):
        self.__caminho = caminho

    def salvar(
        self,
        usuario: Usuario
    ):

        usuarios = JsonManager.carregar(
            self.__caminho
        )

        for u in usuarios:

            if u["id"] == usuario.id:
                raise ValueError(
                    "Usuário já existe."
                )

        usuarios.append(
            usuario.to_dict()
        )

        JsonManager.salvar(
            self.__caminho,
            usuarios
        )

    def listar(self):

        dados = JsonManager.carregar(
            self.__caminho
        )

        usuarios = []

        for d in dados:

            if d["plano"] == "PlanoPremium":
                plano = PlanoPremium()
            else:
                plano = PlanoFree()

            usuarios.append(
                Usuario.from_dict(
                    d,
                    plano
                )
            )

        return usuarios

    def buscar_por_id(
        self,
        id_usuario: str
    ):

        for usuario in self.listar():

            if usuario.id == id_usuario:
                return usuario

        return None

    def remover(
        self,
        id_usuario: str
    ):

        usuarios = JsonManager.carregar(
            self.__caminho
        )

        usuarios = [
            u
            for u in usuarios
            if u["id"] != id_usuario
        ]

        JsonManager.salvar(
            self.__caminho,
            usuarios
        )