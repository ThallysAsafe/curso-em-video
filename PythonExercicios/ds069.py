cont = 0
qmasc = 0
qfem = 0
while True:
    print('===========' * 8)
    print('CADASTRE UMA PESSOA')
    print('===========' * 8)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).upper()
    print('===========' * 8)
    x = str(input('Quer continuar: [S/N]')).upper().strip()
    if x != 'SN':
        x = str(input('Quer continuar: [S/N]')).upper().strip()
    if idade > 18:
        cont += 1
        qmasc += 1
        qfem += 1
    elif sexo == 'M':
        qmasc += 1
    elif sexo == 'F' and idade < 20:
        qfem += 1
    if x == 'N':
        break
print('======== FIM DO PROGRAMA ========')
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {qmasc}, homens cadastrados')
print(f'E temos {qfem} mulheres com menores de 20 anos!')








