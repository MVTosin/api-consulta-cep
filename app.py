def validar_cpf(cpf):
	return len(cpf) == 11

cpf = input("Digite o CPF: ")

if validar_cpf(cpf):
	print("CPF válido")

else:
	print("CPF inválido")