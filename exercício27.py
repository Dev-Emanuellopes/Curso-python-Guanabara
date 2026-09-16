nome = input('Digite seu nome completo: ')
nome = nome.strip()
print('Primeiro nome: {}'.format(nome.split()[0]))
print('Último nome: {}'.format(nome.split()[-1]))