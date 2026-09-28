frase = input("Digite uma frase: ").strip().upper()
juntando = frase.replace(" ", "")
inverso = juntando[::-1]
if juntando == inverso:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
