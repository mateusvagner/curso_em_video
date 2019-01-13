# Sorteando um entre 4 alunos para apagar o quadro
import random

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
indice = random.randint(0, 3)
escolhido = random.choice(alunos)
print('O aluno escolhido foi: {}'.format(alunos[indice]))
print(indice)
print('O aluno escolhido pelo ~choice~ foi: {}'.format(escolhido))
