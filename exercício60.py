import math
n = int(input("Digite um número inteiro para descobrir seu fatorial: "))
print("{}! = {}".format(n, math.factorial(n)))
sair_ou_continuar = input("Aperte 1 para continuar e 0 para sair: ")
while not sair_ou_continuar == "0":
    n = int(input("Digite um número inteiro para descobrir seu fatorial: "))
    print("{}! = {}".format(n, math.factorial(n)))
    sair_ou_continuar = input("Aperte 1 para continuar e 0 para sair: ")
