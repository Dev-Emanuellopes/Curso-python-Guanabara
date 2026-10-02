n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
print("[1] Somar")
print("[2] Multiplicar")
print("[3] Maior")
print("[4] Novos números")
print("[5] Sair do programa")
opção = int(input("Escolha uma opção: "))
while not opção == 5:
    if opção == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é {}".format(n1, n2, soma))
        print("=-==-==-==-==-==-==-==-==-==-==-==-==")
    elif opção == 2:
        multiplicação = n1 * n2
        print("A multiplicação entre {} e {} é {}".format(n1, n2, multiplicação))
        print("=-==-==-==-==-==-==-==-==-==-==-==-==")
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {}, o maior valor é {}".format(n1, n2, maior))
        print("=-==-==-==-==-==-==-==-==-==-==-==-==")
    elif opção == 4:
        print("Informe os números novamente:")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    else:
        print("Opção inválida! Tente novamente.")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do programa")
    opção = int(input("Escolha uma opção: "))