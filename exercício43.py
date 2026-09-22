# Calculadora simples de IMC (Índice de Massa Corporal)
kilo = float(input("Digite o seu peso em quilogramas: "))
altura = float(input("Digite a sua altura em metros: "))
imc = kilo / (altura ** 2)
if imc < 18.5:
    print("Você está abaixo do peso. Seu IMC é: {:.2f}".format(imc))
elif imc < 24.9:
    print("Você está com o peso normal. Seu IMC é: {:.2f}".format(imc))
elif imc < 29.9:
    print("Você está com sobrepeso. Seu IMC é: {:.2f}".format(imc))
elif imc < 39.9:
    print("Você está com obesidade. Seu IMC é: {:.2f}".format(imc))
else:
    print("Você está com obesidade mórbida. Seu IMC é: {:.2f}".format(imc))
