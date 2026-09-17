velocidade = int(input("Digite a velocidade do carro em km/h: "))
if velocidade > 80:
    print("Você foi multado! O valor da multa é de R$ {:.2f}".format((velocidade - 80) * 7))
else:
    print("Parabéns! Você está dentro do limite de velocidade.")