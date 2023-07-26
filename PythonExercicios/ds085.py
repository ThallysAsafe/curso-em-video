num = 0
lista = [[], []]
for i in range(1, 8):
    num = int(input(f'Digite um {i}º numero inteiro: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[1].sort()
lista[0].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')