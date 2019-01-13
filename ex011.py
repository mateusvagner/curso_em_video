# Pintando parede
l = float(input('Informe a largura da parede em metros: '))
h = float(input('Informe a altura da parede em metros: '))
r = float(input('Informe o rendimento da tinta em metros/litros: '))
print('A parede mede {} m² e serão necessários {} litros de tinta'.format(l*h, l*h/r))
