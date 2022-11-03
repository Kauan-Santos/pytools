from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar('kauan.santos2225@gmail.com',
    'kasantos.business@gmail.com',
    'Curso Python Pro',
    'Conteudo do curso de python'
    )
    assert 'kauan.santos2225@gmail.com' in resultado