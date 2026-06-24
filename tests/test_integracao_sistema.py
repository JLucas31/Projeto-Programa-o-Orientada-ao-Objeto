from src.artista import Artista
from src.musica import Musica
from src.usuario import Usuario
from src.playlist import Playlist
from src.plano_premium import PlanoPremium


def test_fluxo_completo_streaming():

    artista = Artista(
        "ART001",
        "Linkin Park",
        "Nu Metal",
        "Estados Unidos"
    )

    musica1 = Musica(
        "MSC001",
        "Numb",
        artista,
        "Nu Metal",
        185,
        "FLAC 44.1kHz 16-bit"
    )

    musica2 = Musica(
        "MSC002",
        "In The End",
        artista,
        "Nu Metal",
        216,
        "FLAC 44.1kHz 16-bit"
    )

    usuario = Usuario(
        "USR001",
        "joao",
        "joao@email.com",
        PlanoPremium()
    )

    playlist = Playlist(
        "PL001",
        "Favoritas",
        usuario
    )

    playlist.adicionar_musica(musica1)
    playlist.adicionar_musica(musica2)

    musica1.reproduzir()
    musica1.reproduzir()
    musica1.curtir()

    assert playlist.quantidade_musicas() == 2
    assert playlist.calcular_duracao() == 401
    assert musica1.reproducoes == 2
    assert musica1.curtidas == 1
    assert usuario.plano.qualidade_audio() == "FLAC 44.1kHz 16-bit"