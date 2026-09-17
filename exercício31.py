kilometragem = float(input("Digite a quilometragem percorrida: "))
if kilometragem <= 200:
    print("O valor da passagem é de R$ {:.2f}".format(kilometragem * 0.50))
else:
    print("O valor da passagem é de R$ {:.2f}".format(kilometragem * 0.45))