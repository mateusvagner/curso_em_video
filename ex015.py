# Aluguel de carros
km = float(input('Qual a distância em km percorrido pelo carro alugado? '))
dias = int(input('Quantos dias ele foi utilizado? '))
print('Você andou {} km durante {} dias e o valor do aluguel é de R${:.2f}.'.format(km, dias, km*0.15+dias*60))
