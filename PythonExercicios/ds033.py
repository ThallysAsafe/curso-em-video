a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))
# Verificando quem é o menor!
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior!
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
# if n1 < n2 < n3:
#    print('O menor numero é {} e o maior numero é {}'.format(n1, n3))
# elif n3 < n2 < n1:
#    print('O menor numero é {} e o maior numero é {}'.format(n3, n1))
# elif n2 < n1 < n3:
#    print('O menor numero é {} e o maior numero é {}'.format(n2, n3))
# elif n3 < n1 < n2:
#   print('O menor numero é {} e o maior numero é {}'.format(n3, n2))
# elif n1 < n3 < n2:
#   print('O menor numero é {} e o maior numero é {}'.format(n1, n2))
# else:
#   print('O menor numero é {} e o maior numero é {}'.format(n2, n1))
