# Tabuada
n = int(input('Digite um  número: '))
print('-'*12)
print('A tabuada do {} é:'.format(n))
for i in range(0, 11):
    print('{} X {:2} = {}'.format(n, i, n*i))
print('-'*12)
