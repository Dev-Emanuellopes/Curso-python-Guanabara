n1 = int(input("Digite um número: "))
if n1 == 2:
    print("O número é primo.")
elif n1 % 2 == 0:
    print("O número não é primo.")
else:
    for c in range(3, int(n1**0.5) + 1, 2):
        if n1 % c == 0:
            print("O número não é primo.")
            break
    else:
        print("O número é primo.")