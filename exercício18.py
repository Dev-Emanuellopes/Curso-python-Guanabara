import math
angulo = float(input("Digite o valor do ângulo em graus: "))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)
print(f"O seno do ângulo é: {seno:.2f}")
print(f"O cosseno do ângulo é: {cosseno:.2f}")
print(f"A tangente do ângulo é: {tangente:.2f}")