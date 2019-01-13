# Programa que lê um número de 0 a 9999 e mostre cada digito separado
# Forma de string
'''
num = input('Digite um número de 0 a 9999: ')
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
'''

# Forma numérica
num2 = int(input('Digite um número de 0 a 9999: '))
u = num2 // 1 % 10
d = num2 // 10 % 10
c = num2 // 100 % 10
m = num2 // 1000 % 10
print('Analisando o número {}'.format(num2))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
