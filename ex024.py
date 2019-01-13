#  Leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
nome = str(input('Digite o nome de uma cidade: ')).strip()
print('A cidade possui o nome "Santo"? {}'.format(nome[:5].lower() == 'santo'))
# nome[:5] vai ler até o 'O'
