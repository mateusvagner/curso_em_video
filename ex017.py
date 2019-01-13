# Catetos e hipotenusas
import math

co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hip = (cp ** 2 + ca ** 2) ** 0.5
print('A hipotenusa dos catetos {} e {} é: {:.2f}'.format(co, ca, hip))
print('A hiponetusa calculada pelo ~math~ é: {:.2f}'.format(math.hypot(co, ca)) )
