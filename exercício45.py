import random
opcoes = ["pedra", "papel", "tesoura"]
while True:
    jogador = input ("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
    if jogador == "sair":
        print("Jogo encerrado.")
        break

    if jogador not in opcoes:
        print("Opção inválida. Tente novamente.")
        continue

    computador = random.choice(opcoes)

    if jogador == computador:
        print(f"Empate! Ambos escolheram {jogador}.")
    elif (jogador == "pedra" and computador == "tesoura") or \
            (jogador == "papel" and computador == "pedra") or \
            (jogador == "tesoura" and computador == "papel"):
        print(f"Você venceu! {jogador} vence {computador}.")
    else:
        print(f"Você perdeu! {computador} vence {jogador}.")