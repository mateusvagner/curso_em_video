# Calculando descontos
valor = float(input('Qual o valor do produto? '))
desc = float(input('Qual o valor do desconto em %? '))
print('O produto custa {}. Com desconto de {}% o valor será de {}.'.format(valor, desc, valor*(1-desc/100)))
