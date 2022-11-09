from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido
import pytest

def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['kauan.santos2225@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'kasantos.business@gmail.com',
        'Curso Python Pro',
        'Conteudo do curso de python'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'kauan']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'kasantos.business@gmail.com',
            'Curso Python Pro',
            'Conteudo do curso de python'
        )
