import pytest

from src.artista import Artista
from src.musica import Musica
from src.usuario import Usuario
from src.playlist import Playlist
from src.plano_free import PlanoFree


@pytest.fixture
def playlist():

    usuario = Usuario(
        "USR001",
        "joao",
        "joao@email.com",
        PlanoFree()
    )

    return Playlist(
        "PL001",
        "Favoritas",
        usuario
    )


@pytest.fixture
def musica():

    artista = Artista(
        "ART001",
        "Linkin Park",
        "Rock",
        "Estados Unidos"
    )

    return Musica(
        "MSC001",
        "Numb",
        artista,
        "Rock",
        185,
        "FLAC 44.1kHz 16-bit"
    )


def test_adicionar_musica(
    playlist,
    musica
):

    playlist.adicionar_musica(musica)

    assert playlist.quantidade_musicas() == 1


def test_nao_adicionar_musica_duplicada(
    playlist,
    musica
):

    playlist.adicionar_musica(musica)
    playlist.adicionar_musica(musica)

    assert playlist.quantidade_musicas() == 1


def test_remover_musica(
    playlist,
    musica
):

    playlist.adicionar_musica(musica)
    playlist.remover_musica(musica)

    assert playlist.quantidade_musicas() == 0


def test_remover_musica_inexistente(
    playlist,
    musica
):

    playlist.remover_musica(musica)

    assert playlist.quantidade_musicas() == 0


def test_calcular_duracao(
    playlist,
    musica
):

    playlist.adicionar_musica(musica)

    assert playlist.calcular_duracao() == 185


def test_calcular_duracao_varias_musicas(
    playlist
):

    artista = Artista(
        "ART001",
        "Linkin Park",
        "Rock",
        "Estados Unidos"
    )

    playlist.adicionar_musica(
        Musica(
            "MSC001",
            "Numb",
            artista,
            "Rock",
            185,
            "MP3 320kbps"
        )
    )

    playlist.adicionar_musica(
        Musica(
            "MSC002",
            "In The End",
            artista,
            "Rock",
            216,
            "FLAC 44.1kHz 16-bit"
        )
    )

    assert playlist.calcular_duracao() == 401