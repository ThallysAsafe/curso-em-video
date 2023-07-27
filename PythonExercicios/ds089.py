ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    r = str(input('Quer continuar: [S/N]'))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    if r in 'Nn':
        break
print(f'{"Nu.":<4}{"Nome":<10} {"Média":>8}')
print('-'*20)
for l in range(0, len(ficha[0])-1):
    for c in range(0, 1):
        print(f'{l:<4}{ficha[l][0]:<10}{ficha[l][2]:>8.1f}')
print('-'*20)
num = 0
while num != 999:
    num = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    for i, l in enumerate(ficha):
            if num == i:
                print(f'Notas de {ficha[num][0]} são {ficha[num][1]}')

print('Fim do programa')