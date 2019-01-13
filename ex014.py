# Conversor de temperatura
cel = float(input('Qual a temperatura em °C? '))
fah = cel * 9 / 5 + 32
print('A temperatura de {:.2f} °C é equivalente a {:.2f} °F.'.format(cel, fah))
