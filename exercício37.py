num = int(input("Digite um número inteiro: "))
base = input("Digite a base (binário, octal ou hexadecimal): ").lower().replace("a", "á")

if base == "binário":
    print("O número {} em binário é {}".format(num, bin(num)[2:]))
elif base == "octal":
    print("O número {} em octal é {}".format(num, oct(num)[2:]))
elif base == "hexadecimal":
    print("O número {} em hexadecimal é {}".format(num, hex(num)[2:].upper()))
else:
    print("Base inválida.")