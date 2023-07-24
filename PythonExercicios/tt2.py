'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
op = int(input('''----AÇÕES----
[1] - PAR OU IMPAR
[2] - POSITIVO OU NEGATIVO
[3] - INTEIRO OU DECIMAL
Digite qual ação queira fazer:'''))
if op == 1:
    if num1 % 2 == 0:
        print(f'{num1} é par')
    else:
        print(f'{num1} é impar')
    if num2 % 2 == 0:
        print(f'{num2} é par')
    else:
        print(f'{num2} é impar')
elif op == 2:
    if num1 > 0:
        print(f'{num1} é positivo')
    else:
        print(f'{num1} é negativo')
    if num2 > 0:
        print(f'{num2} é positivo')
    else:
        print(f'{num2} é negativo')
elif op == 3:
    if num1 // 1 == num1:
        print(f'{num1} é inteiro')
    else:
        print(f'{num1} é decimal')
    if num2 // 1 == num2:
        print(f'{num2} é inteiro')
    else:
        print(f'{num2} é decimal')
else:
    print('AÇÃO INVÁLIDA!')

