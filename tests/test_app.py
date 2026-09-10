from app import validar_cpf


def test_cpf_valido():
    assert validar_cpf("12345678901") == True


def test_cpf_invalido():
    assert validar_cpf("123") == False