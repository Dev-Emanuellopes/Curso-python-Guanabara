import datetime
ano_atual = datetime.datetime.now().year
for c in range (1, 8):
    ano_de_nascimento = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(c)))
    idade = ano_atual - ano_de_nascimento
    if idade < 18:
        print(f"Você tem {idade} anos. Ainda não atingiu a maioridade.")
    elif idade == 18:
        print(f"Você tem {idade} anos. Você atingiu a maioridade este ano.")
    else:
        print(f"Você tem {idade} anos. Você já atingiu a maioridade.")