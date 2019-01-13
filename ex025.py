# leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = str(input('Digite o nome de uma cidade: ')).strip()
print('Seu nome tem "Silva"? {}'.format('silva' in nome.lower()))
