from repositories.artista_repository import ArtistaRepository
from repositories.musica_repository import MusicaRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.playlist_repository import PlaylistRepository

from src.artista import Artista
from src.musica import Musica
from src.usuario import Usuario
from src.playlist import Playlist

from src.plano_free import PlanoFree
from src.plano_premium import PlanoPremium


class StreamMusicApp:

    def __init__(self):

        self.artista_repo = ArtistaRepository()
        self.usuario_repo = UsuarioRepository()
        self.musica_repo = MusicaRepository(self.artista_repo)

        self.playlist_repo = PlaylistRepository(self.usuario_repo,self.musica_repo)

    def executar(self):

        while True:

            print("\n" + "=" * 50)
            print("         STREAM MUSIC")
            print("=" * 50)

            print("1 - Gerenciar Artistas")
            print("2 - Gerenciar Músicas")
            print("3 - Gerenciar Usuários")
            print("4 - Gerenciar Playlists")
            print("5 - Relatórios")
            print("0 - Sair")

            opcao = input("\nEscolha uma opção: ")

            match opcao:

                case "1":
                    self.menu_artistas()

                case "2":
                    self.menu_musicas()

                case "3":
                    self.menu_usuarios()

                case "4":
                    self.menu_playlists()

                case "5":
                    self.menu_relatorios()

                case "0":
                    print("\nEncerrando sistema...")
                    break

                case _:
                    print("\nOpção inválida.")


    def menu_artistas(self):

        while True:

            print("\n=== ARTISTAS ===")

            print("1 - Cadastrar artista")
            print("2 - Listar artistas")
            print("3 - Buscar artista")
            print("4 - Remover artista")
            print("0 - Voltar")

            opcao = input("\nEscolha: ")

            if opcao == "1":

                id_ = input("ID: ")
                nome = input("Nome: ")
                genero = input("Gênero: ")
                pais = input("País: ")

                artista = Artista(id_, nome, genero, pais)

                self.artista_repo.salvar(artista)

                print("Artista cadastrado.")

            elif opcao == "2":

                artistas = (self.artista_repo.listar())

                for artista in artistas:
                    print(artista)

            elif opcao == "3":

                id_ = input("ID do artista: ")

                artista = (self.artista_repo.buscar_por_id(id_))

                if artista:

                    print(artista)

                else:

                    print("Artista não encontrado.")

            elif opcao == "4":

                id_ = input("ID do artista: ")

                self.artista_repo.remover(id_)

                print("Removido.")

            elif opcao == "0":
                break

    def menu_usuarios(self):

        while True:

            print("\n=== USUÁRIOS ===")

            print("1 - Cadastrar usuário")
            print("2 - Listar usuários")
            print("3 - Buscar usuário")
            print("4 - Remover usuário")
            print("0 - Voltar")

            opcao = input("\nEscolha: ")

            if opcao == "1":

                id_ = input("ID: ")
                username = input("Username: ")
                email = input("Email: ")

                print("\nPlano:")
                print("1 - Free")
                print("2 - Premium")

                plano_opcao = input()

                if plano_opcao == "1":
                    plano = PlanoFree()
                else:
                    plano = PlanoPremium()

                usuario = Usuario(id_, username, email, plano)

                self.usuario_repo.salvar(usuario)

                print("Usuário cadastrado.")

            elif opcao == "2":

                usuarios = (self.usuario_repo.listar())

                for usuario in usuarios:
                    print(usuario)

            elif opcao == "3":

                id_ = input("ID do usuário: ")

                usuario = (self.usuario_repo.buscar_por_id(id_))

                print(usuario)

            elif opcao == "4":

                id_ = input("ID do usuário: ")

                self.usuario_repo.remover(id_)

                print("Usuário removido.")

            elif opcao == "0":
                break

    def menu_musicas(self):

        while True:

            print("\n=== MÚSICAS ===")

            print("1 - Cadastrar música")
            print("2 - Listar músicas")
            print("3 - Reproduzir música")
            print("4 - Curtir música")
            print("5 - Remover música")
            print("0 - Voltar")

            opcao = input("\nEscolha: ")

            if opcao == "1":

                id_ = input("ID: ")
                titulo = input("Título: ")
                genero = input("Gênero: ")

                try:
                    duracao = int(input("Duração (segundos): "))

                except ValueError:
                    print("Erro: digite um número válido.")

                formato = input("Formato de áudio: ")

                artista_id = input("ID do artista: ")

                artista = (self.artista_repo.buscar_por_id(artista_id))

                if artista is None:
                    print("Artista não encontrado.")
                    continue

                musica = Musica(
                    id_,
                    titulo,
                    artista,
                    genero,
                    duracao,
                    formato
                )

                self.musica_repo.salvar(musica)

                print("Música cadastrada.")

            elif opcao == "2":

                for musica in (self.musica_repo.listar()):
                    print(musica)

            elif opcao == "3":

                id_ = input("ID da música: ")

                musica = (self.musica_repo.buscar_por_id(id_))

                if musica:
                    musica.reproduzir()

                    print("Reprodução registrada.")

            elif opcao == "4":

                id_ = input("ID da música: ")

                musica = (self.musica_repo.buscar_por_id(id_))

                if musica:
                    musica.curtir()

                    print("Curtida registrada.")

            elif opcao == "5":

                id_ = input("ID da música: ")

                self.musica_repo.remover(id_)

            elif opcao == "0":
                break

    def menu_playlists(self):

        while True:

            print("\n=== PLAYLISTS ===")

            print("1 - Criar playlist")
            print("2 - Listar playlists")
            print("3 - Remover playlist")
            print("0 - Voltar")

            opcao = input("\nEscolha: ")

            if opcao == "1":

                id_ = input("ID: ")
                nome = input("Nome: ")

                usuario_id = input("ID do criador: ")

                usuario = (self.usuario_repo.buscar_por_id(usuario_id))

                if usuario is None:

                    print("Usuário não encontrado.")

                    continue

                playlist = Playlist(
                    id_,
                    nome,
                    usuario
                )

                self.playlist_repo.salvar(playlist)

                print("Playlist criada.")

            elif opcao == "2":

                for playlist in (self.playlist_repo.listar()):
                    print(playlist)

            elif opcao == "3":

                id_ = input("ID da playlist: ")

                self.playlist_repo.remover(id_)

            elif opcao == "0":
                break

    def menu_relatorios(self):

        print("\n=== RELATÓRIOS ===")

        print(
            f"Artistas: "
            f"{len(self.artista_repo.listar())}"
        )

        print(
            f"Músicas: "
            f"{len(self.musica_repo.listar())}"
        )

        print(
            f"Usuários: "
            f"{len(self.usuario_repo.listar())}"
        )

        print(
            f"Playlists: "
            f"{len(self.playlist_repo.listar())}"
        )

if __name__ == "__main__":

    app = StreamMusicApp()

    app.executar()