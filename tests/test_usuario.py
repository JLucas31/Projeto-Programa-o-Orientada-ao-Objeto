import pytest

from src.usuario import Usuario
from src.plano_free import PlanoFree


@pytest.fixture
def usuario():

    return Usuario(
        "USR001",
        "joao",
        "joao@email.com",
        PlanoFree()
    )


@pytest.mark.parametrize(
    "email",
    [
        "teste@gmail.com",
        "usuario@hotmail.com",
        "abc@empresa.com.br"
    ]
)
def test_email_valido(email):

    assert Usuario.validar_email(email)


@pytest.mark.parametrize(
    "email",
    [
        "",
        "abc",
        "@",
        "gmail.com",
        "@gmail.com",
        "abc@gmail"
    ]
)

def test_email_invalido(email):

    assert not Usuario.validar_email(email)


def test_criacao_usuario_email_invalido():

    with pytest.raises(ValueError):

        Usuario(
            "USR001",
            "joao",
            "email_invalido",
            PlanoFree()
        )


def test_criar_playlist(usuario):

    usuario.criar_playlist("Rock")

    assert len(usuario.listar_playlists()) == 1


def test_lista_playlists_retorna_copia(usuario):

    usuario.criar_playlist("Rock")

    playlists = usuario.listar_playlists()

    playlists.clear()

    assert len(usuario.listar_playlists()) == 1