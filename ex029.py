# leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa
# vai custar R$7,00 por cada Km acima do limite.

v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('O carro estava à {:.1f} km/h.'.format(v))
    print('A multa será de R$ {:.2f}.'.format((v - 80)*7))
else:
    print('O carro estava a {:.1f} km/h. Tudo certo!'.format(v))
print('Tenha um bom dia. Dirija com segurança')
