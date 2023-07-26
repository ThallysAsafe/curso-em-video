princ = []
temp = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso, em Kg: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Quer continuar: '))
    if r in 'Nn':
        break
    elif r not in 'SsNn':
        while r not in 'SsNn':
            r = str(input('Quer continuar: '))
        if r in 'Nn':
            break
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi {mai} Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print(f'\nO menor peso foi {men} Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end='')


