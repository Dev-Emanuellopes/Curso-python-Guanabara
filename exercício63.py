
n = int(input("Quantos termos você quer mostrar? "))

t1 = 0
t2 = 1
cont = 1
while cont <= n:
    print(t1, end="")
    if cont < n:
        print(" → ", end="")
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1

print(" → FIM")
