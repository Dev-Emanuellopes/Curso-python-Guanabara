from random import randint
n = randint(1, 10)
s = 0
jogador = int(input("Digite um número entre 1 e 10: "))
while not jogador == n:
    print("Você errou! Tente novamente.")
    s += 1
    jogador = int(input("Digite um número entre 1 e 10: "))
print("Parabéns! Você acertou!")
print("Você precisou de", s+1, "tentativas para acertar o número", n)