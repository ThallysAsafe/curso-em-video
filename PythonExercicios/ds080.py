listnum = []
for v in range(0, 5):
    num = (int(input('Digite um valor: ')))
    if v == 0 or num > listnum[-1]:
        print(f'Adicionando {num}, ao final da lista')
        listnum.append(num)
    else:
        pos = 0
        while pos < len(listnum):
            if num <= listnum[pos]:
                listnum.insert(pos, num)
                print(f'Adicionando {num} na posição {pos}...')
                break
            pos += 1
print('='*30)
print(f'Os valores digitados foram {listnum}')
