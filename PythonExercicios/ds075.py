total = (int(input('Digite outro numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite outro numero: ')))
print(f'Voce digitou os valores: {total}')
print(f'O número 9 apareceu {total.count(9)} vezes')
if 3 in total:
    print(f'O número 3 apareceu primeiramente na {total.index(3)+1}ª posição.')
else:
    print('O número 3 apareceu primeiramente em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in total:
    if n % 2 == 0:
        print(n, end=' ')
