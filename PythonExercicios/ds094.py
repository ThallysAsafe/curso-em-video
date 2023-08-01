pessoa = {}
total = []
acimamedia = []
soma = 0
while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper().strip()
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    if pessoa['sexo'] not in 'FM':
        while pessoa['sexo'] not in 'FM':
            pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper().strip()
    total.append(pessoa.copy())
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
media = soma / len(total)
print('-='*30)
print(f'-O grupo tem {len(total)}')
print(f'-A média de idade desse grupo de pessoas é: {media}')
print(f'-As Mulheres cadastradas foram: ', end='')
for k in total:
    if k['idade'] >= media:
        acimamedia.append(k)
    if k['sexo'] in 'F':
        print(f'{k["nome"]}', end='')
print(f'\n-Pessoas que estão acima da idade media:')
for i in acimamedia:
    print(i)
