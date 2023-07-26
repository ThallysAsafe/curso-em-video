num = []
while True:
    num.append(int(input('Digite um valor: ')))
    r = str(input('Quer Continuar? [S/N]'))
    if r in 'Nn':
        break
print(f'Foram digitados {len(num)} numeros!')
num.sort(reverse=True)
print(f'Lista em ordem decrescente: {num}')
c = num.count(5)
if c >= 1:
    print(f'O valor 5 está presente na lista.')
else:
    print(f'O valor 5 não está presente na lista.')
