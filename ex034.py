# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Qual o salário do funcionário? R$ '))
if s <= 1250:
    aumento = s * 1.15
else:
    aumento = s * 1.10
print('O novo salário é de R$ {:.2f} para quem recebia salário de R$ {:.2f}.'.format(aumento, s))
