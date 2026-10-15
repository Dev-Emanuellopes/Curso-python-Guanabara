termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

for i in range(10):
    print(termo)
    termo += razao

adicionar = int(input("Quantos termos você quer adicionar? "))

for i in range(adicionar):
    print(termo)
    termo += razao

if adicionar == 0:
    print("Nenhum termo adicional foi adicionado.")
