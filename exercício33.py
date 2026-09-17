num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
if num1 >= num2 and num1 >= num3:
    print("O maior número é: {} e o menor é: {}".format(num1, min(num2, num3)))
elif num2 >= num1 and num2 >= num3:
    print("O maior número é: {} e o menor é: {}".format(num2, min(num1, num3)))
else:
    print("O maior número é: {} e o menor é: {}".format(num3, min(num1, num2)))