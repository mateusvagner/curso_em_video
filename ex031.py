# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = float(input('Qual a distância percorrida? '))
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print('O preço da passagem é R$ {:.2f}'.format(preco))

# outra maneira
preco = dist * 0.5 if dist <= 200 else dist * 0.45
print(preco)
