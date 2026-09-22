casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do salário: "))
anos = int(input("Digite o número de anos para pagar: "))
prestacao_mensal = casa / (anos * 12)
if prestacao_mensal > (salario * 0.3):
    print("Empréstimo não concedido.")
else:
    print("O valor da prestacão mensal é igual a {:.2f} e o seu empréstimo foi concedido.".format(prestacao_mensal))