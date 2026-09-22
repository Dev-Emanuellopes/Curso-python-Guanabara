from datetime import date
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = date.today().year - ano_nascimento
if idade < 18:
    print(f"Você tem {idade} anos. Ainda não atingiu o tempo de se alistar! Faltam {18 - idade} anos.")

elif idade == 18:
    print(f"Você tem {idade} anos. Está na hora de se alistar!")

else:
    print(f"Você tem {idade} anos. Já passou {idade - 18} anos do tempo de se alistar!")