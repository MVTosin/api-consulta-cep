def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if not cpf.isdigit():
        return False

    return len(cpf) == 11


def solicitar_cpf():
    cpf = input("Digite o CPF: ")
    return validar_cpf(cpf)


async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    resultado = solicitar_cpf()

    if resultado:
        print("CPF válido")
    else:
        print("CPF inválido")