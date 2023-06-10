n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
if n1 < n2 < n3:
    print('O menor numero é {} e o maior numero é {}'.format(n1, n3))
elif n3 < n2 < n1:
    print('O menor numero é {} e o maior numero é {}'.format(n3, n1))
elif n2 < n1 < n3:
    print('O menor numero é {} e o maior numero é {}'.format(n2, n3))
elif n3 < n1 < n2:
    print('O menor numero é {} e o maior numero é{}'.format(n3, n2))
elif n1 < n3 < n2:
    print('O menor numero é {} e o maior numero é {}'.format(n1, n2))
else:
    print('O menor numero é {} e o maior numero é {}'.format(n2, n1))
