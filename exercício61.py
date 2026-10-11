termo = int(input("Digite o termo que deseja calcular: "))
razao = int(input("Digite a razão da PA: "))
cont = 1
while not cont <= 10:
    print("O termo {} da PA é: {}".format(cont, termo))
    cont += 1
    termo += razao