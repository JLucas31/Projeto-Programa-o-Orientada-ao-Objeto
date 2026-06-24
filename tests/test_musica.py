import pytest

from src.artista import Artista
from src.musica import Musica


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


def test_reproduzir_musica(musica):

    musica.reproduzir()

    assert musica.reproducoes == 1


def test_multiplas_reproducoes(musica):

    for _ in range(1000):
        musica.reproduzir()

    assert musica.reproducoes == 1000


def test_curtir_musica(musica):

    musica.curtir()

    assert musica.curtidas == 1


def test_multiplas_curtidas(musica):

    for _ in range(500):
        musica.curtir()

    assert musica.curtidas == 500


@pytest.mark.parametrize(
    "formato",
    [
        "MP3 320kbps",
        "AAC 256kbps",
        "FLAC 44.1kHz 16-bit",
        "FLAC 96kHz 24-bit"
    ]
)
def test_alterar_formato_audio(
    musica,
    formato
):

    musica.alterar_formato(formato)

    assert musica.formato_audio == formato


def test_artista_associado(musica):

    assert musica.artista.nome == "Linkin Park"


def test_duracao_musica(musica):

    assert musica.duracao_segundos == 185