dic = {'Nome': str(input('Nome do Jogador: '))}
partidas = int(input(f'Quantas partidas {dic["Nome"]} jogou: '))
gols1 = []
soma = 0
for i in range(1, partidas+1):
        gol = (int(input(f'Quantos gols {dic["Nome"]} fez na {i}ª partida?')))
        soma += gol
        gols1.append(gol)
dic['gols'] = gols1
dic['total'] = soma
print('-='*30)
print(dic)
print('-='*30)
for k, v in dic.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {dic["Nome"]} jogou {partidas} partidas.')
for i in range(0, partidas):
    print(f'     => Na Partida {i+1}, fez {dic["gols"][i]}.')
print(f'Foi um total de {dic["total"]} gols.')

