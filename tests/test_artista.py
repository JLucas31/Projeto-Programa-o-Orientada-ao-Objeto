import pytest

from src.artista import Artista


@pytest.fixture
def artista():
    return Artista(
        "ART001",
        "Linkin Park",
        "Nu Metal",
        "Estados Unidos",
        100
    )


def test_adicionar_seguidor(artista):

    artista.adicionar_seguidor()

    assert artista.seguidores == 101


def test_remover_seguidor(artista):

    artista.remover_seguidor()

    assert artista.seguidores == 99


def test_nao_permitir_seguidores_negativos():

    artista = Artista(
        "ART002",
        "Imagine Dragons",
        "Nu Metal",
        "Estados Unidos",
        0
    )

    artista.remover_seguidor()

    assert artista.seguidores == 0


def test_multiplas_operacoes_de_seguidores(artista):

    for _ in range(10):
        artista.adicionar_seguidor()

    for _ in range(5):
        artista.remover_seguidor()

    assert artista.seguidores == 105