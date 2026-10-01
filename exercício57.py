sexo = input("Digite seu sexo (f/m): ").lower()
while " ":
    if sexo == "f" or sexo == "m":
        print("Sexo registrado com sucesso.")
        break
    else:
        print("Sexo inválido. Por favor, digite 'f' para feminino ou 'm' para masculino.")
        sexo = input("Digite seu sexo (f/m): ").lower()