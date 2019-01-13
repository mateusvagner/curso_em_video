# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))
if a < b + c and b < a + c and c < a + b:
    print('Os lados dados podem formar um triângulo')
else:
    print('Não formam triângulo')
