import random
n = int(input("Tente adivinhar o número que estou pensando entre 1 e 5: "))
if n == random.randint(1, 5):
    print("Parabéns! Você acertou!")
else:
    print("Que pena! Você errou!")
input("O número que pensei era {}!".format(random.randint(1, 5)))
