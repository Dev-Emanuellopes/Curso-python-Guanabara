idade = int(input("Digite a idade do nadador: "))
if idade <= 9:
    print("Categoria: MIRIM")
elif idade <= 14:
    print("Categoria: INFANTIL")
elif idade <= 19:
    print("Categoria: JÚNIOR")
elif idade <= 25:
    print("Categoria: SÊNIOR")
else:
    print("Categoria: MASTER")
    