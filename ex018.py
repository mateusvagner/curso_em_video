# seno, cosseno e tangente
import math

a = float(input('Digite o ângulo em graus: '))
print('O SENO de {} é: {:.2f}'.format(a, math.sin(math.radians(a))))
print('O COSSENO de {} é: {:.2f}'.format(a, math.cos(math.radians(a))))
print('A TANGENTE de {} é: {:.2f}'.format(a, math.tan(math.radians(a))))
