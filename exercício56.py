soma_idades = 0
maior_idade_homem = 0
nome_maior_idade_homem = ""
menor_mulher = 0

for i in range(1, 5):
    nome = input("Digite o nome da {}ª pessoa: ".format(i))
    idade = int(input("Digite a idade da {}ª pessoa: ".format(i)))
    sexo = input("Digite o sexo da {}ª pessoa (M/F): ".format(i)).strip().lower()
    
    soma_idades += idade

    if sexo == "m":
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_maior_idade_homem = nome

    if sexo == "f" and idade < 20:
        menor_mulher += 1

print("A maior idade entre os homens é {} anos e quem tem essa idade é o {}".format(
    maior_idade_homem, nome_maior_idade_homem))
print("A média das idades é igual a {:.2f}".format(soma_idades / 4))
print("A quantidade de mulheres com menos de 20 anos é igual a {}!".format(menor_mulher))