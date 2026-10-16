num = int(input("Digite um número inteiro[Digite 0 para sair]: "))
soma = 0
cont = 0
maior = 0
menor = 0
while not num == 0:
    soma+= num
    cont+= 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    num = int(input("Digite um número inteiro[Digite 0 para sair]: "))
print(f"A média dos números digitados é: {soma/cont if cont > 0 else 0}")
print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")