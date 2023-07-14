cont = 0
qmasc = 0
qfem = 0
print('===========' * 8)
print('CADASTRE UMA PESSOA')
print('===========' * 8)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).upper()
    print('===========' * 8)
    x = ' '
    while x not in 'SN':
        x = str(input('Quer continuar: [S/N]')).upper().strip()[0]
    if idade > 18:
        cont += 1
    if sexo == 'M':
        qmasc += 1
    if sexo == 'F' and idade < 20:
        qfem += 1
    if x == 'N':
        break
print('======== FIM DO PROGRAMA ========')
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {qmasc}, homens cadastrados')
print(f'E temos {qfem} mulheres com menores de 20 anos!')








