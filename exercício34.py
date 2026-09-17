salario = float(input("Digite o salário do funcionário: "))
if salario >= 1250:
    print("O aumento será de 10% e o novo salário será: R${:.2f}".format(salario * 1.10))
else:
    print("O aumento será de 15% e o novo salário será: R${:.2f}".format(salario * 1.15))