maioridadehomem = 0
médiaidade = 0
totmulher20 = 0
nomevelho = ''
somaidade = 0
for c in range(1, 5):
    print('-----{}ºPESSOA-------'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('''Sexo: 
    [M] - Masculino
    [F] - Feminino
    Digite: ''')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A idade média do grupo é {}' .format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
if totmulher20 == 1:
    print('Tem {} mulher com menos de 20 anos de idade'.format(totmulher20))
elif totmulher20 > 1:
    print('Tem {} mulheres com menos de 20 anos de idade'.format(totmulher20))
else:
    print('Não tem mulheres com menos de 20 anos de idade')
