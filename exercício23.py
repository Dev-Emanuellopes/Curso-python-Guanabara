# Tive dúvidas no exercício, então pesquisei na internet e encontrei a solução.
num = int(input("Digite um número inteiro entre 0 e 9999: "))

print("Unidade desse número é igual a {}".format(num % 10))
print("Dezena desse número é igual a {}".format((num // 10) % 10))
print("Centena desse número é igual a {}".format((num // 100) % 10))
print("Milhar desse número é igual a {}".format((num // 1000) % 10))
