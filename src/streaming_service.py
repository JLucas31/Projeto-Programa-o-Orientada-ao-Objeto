class StreamingService:

    def __init__(self):

        self.artistas = []
        self.musicas = []
        self.usuarios = []
        self.playlists = []

    def cadastrar_artista(self, artista):
        self.artistas.append(artista)

    def cadastrar_musica(self, musica):
        self.musicas.append(musica)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def cadastrar_playlist(self, playlist):
        self.playlists.append(playlist)

    def buscar_musica(self, titulo):

        for musica in self.musicas:

            if musica.titulo.lower() == titulo.lower():
                return musica

        return None

    def listar_catalogo(self):

        return self.musicas

    def reproduzir_musica(self, musica):

        musica.reproduzir()

    def curtir_musica(self, musica):

        musica.curtir()