# Sorteando uma ordem
from random import shuffle, sample

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
alunos2 = sample(alunos, 4)   # o sample cria uma nova lista sem modificar a outra
shuffle(alunos)     # embaralha a própria lista

print('A ordem de apresentação é: {} (sample)'.format(alunos2))
print('A ordem de apresentação é: {} (shuffle)'.format(alunos))
