def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if not cpf.isdigit():
        return False

    return len(cpf) == 11


async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    cpf = input("Digite o CPF: ")

    if validar_cpf(cpf):
        print("CPF válido")
    else:
        print("CPF inválido")