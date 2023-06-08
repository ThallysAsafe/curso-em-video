from random import choice
print('Programa pra sortear quem vai apagar o quadro')
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
lista = (a, b, c, b)
escolhido = choice(lista)
print('O sorteado foi {}'.format(escolhido))
