num = int(input('Digite um número inteiro: '))
print(f'O núnero digitado foi: {num}\n'
      f'O dobro de {num} dobro é: {2 * num}\n'
      f'O triplo de {num} é: {3 * num}\n'
      f'A raíz quadrada de {num} é: {num ** 0.5:.2f}\n\n')

print('O núnero digitado foi: {}\nSeu dobro é: {}\nSeu triplo é: {}\nSua raiz quadrada é: {:.2f}'
      .format(num, 2*num, 3*num, pow(num, 1/2)))
