def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if not cpf.isdigit():
        return False

    return len(cpf) == 11


cpf = input("Digite o CPF: ")

if validar_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")