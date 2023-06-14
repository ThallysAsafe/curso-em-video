import math
num = int(input('Digite um numero inteiro qualquer? '))
print('''Escolha uma das bases pra sua conversão: 
[1] - para binário
[2] - para octal
[3] - para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA')
