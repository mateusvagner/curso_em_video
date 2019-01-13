# programa que lê o nome completo de uma pessoa
nome = str(input('Digite seu nome completo: ')).strip()  # a função .strip() retira os espaços antes e depois
print('O seu nome em letras MAIÚSCULAS é: {}'.format(nome.upper()))
print('O seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))  # .count(' ') conta espaços
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))  # .find(' ') vai procurar tantos caracteres até o primeiro espaço
separa = nome.split()
print(len(separa[0]))
