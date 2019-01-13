# Conversor de Moedas
r = float(input('Digite quantos reais você tem: R$'))
d = float(input('Digite a cotação do dólar: US$'))
print('US$1.00 vale R${:.2f}.'.format(d))
print('Com R${:.2f} você pode comprar U$ {:.2f}.'.format(r, r/d))
