from unittest.mock import patch

from src.app import validar_cpf, solicitar_cpf


def test_cpf_valido():
    assert validar_cpf("12345678901") == True


def test_cpf_invalido():
    assert validar_cpf("123") == False


def test_cpf_com_letras():
    assert validar_cpf("1234567890A") == False


@patch("builtins.input", return_value="12345678901")
def test_entrada_cpf(mock_input):
    resultado = solicitar_cpf()

    assert resultado == True
    mock_input.assert_called_once_with("Digite o CPF: ")