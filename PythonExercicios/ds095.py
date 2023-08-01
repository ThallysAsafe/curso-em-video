dic = {}
soma = 0
gols = list()
cont = 0
time = list()
while True:
    cont += 1
    dic.clear()
    dic['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas Partidas {dic["Nome"]} Jogou? '))
    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {i + 1}: ')))
    dic['Gols'] = gols[:]
    dic['total'] = sum(gols)
    time.append(dic.copy())
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
    elif r not in 'Ss':
        while True:
            r = str(input('Quer continuar? [S/N]'))
            if r in 'NnSs':
                break
print('-=' * 30)
print(f'{"Nu.":<4}{"Nome":<10}{"Gols":>10}{"total":>15}')
print('--' * 30)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
pes = 0
while pes != 999:
    pes = int(input('Mostrar Dados de Qual Jogador? '))
    for k, l in enumerate(dic['Nome']):
        if k == pes:
            print(f'-Levantamento do Jogador {dic["Nome"][pes]}')
            for i in range(partidas):
                print(f'    No Jogo {i} fez {dic["Gols"][i]} gols')
        else:
            print('Erro no Código!')
print('<===== VOLTE SEMPRE =====>')
