a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))

for c in range(1, 11):
    print(f"{c}º termo: {a1 + (c - 1) * r}")