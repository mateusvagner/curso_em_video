# jogo da adivinhação
from random import randint
from time import sleep
n = randint(0, 5)
print('*-' * 12 + '*')
print('Vou pensar em um número.')
print('*-' * 12 + '*')
# print(n)
chute = int(input('Tente adivinhar o número de 0 a 5: '))
print('Processando...')
sleep(2)
if chute == n:
    print('Parabéns! Você acertou.')
else:
    print('Tente de novo! Pensei em {}.'.format(n))
