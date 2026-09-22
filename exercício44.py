valor_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("Digite a forma de pagamento (1 - à vista (dinheiro), 2 - parcelado (2x), 3 - à vista (cartão), 4 - parcelado (3x ou mais)): "))
if forma_de_pagamento == 1:
    desconto = valor_produto * 0.10
    valor_final = valor_produto - desconto
    print("Você escolheu pagar à vista em dinheiro. O valor final com desconto é: R$ {:.2f}".format(valor_final))
elif forma_de_pagamento == 2:
    valor_final = valor_produto
    print("Você escolheu parcelar em 2x. O valor final é: R$ {:.2f}".format(valor_final))
elif forma_de_pagamento == 3:
    valor_final = valor_produto * 0.95
    print("Você escolheu pagar à vista no cartão. O valor final é: R$ {:.2f}".format(valor_final))
elif forma_de_pagamento == 4:
    valor_final = valor_produto * 1.20
    print("Você escolheu parcelar em 3x ou mais. O valor final é: R$ {:.2f}".format(valor_final))