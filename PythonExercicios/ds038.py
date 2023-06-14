num = int(input('Digite o primeiro numero inteiro: '))
num2 = int(input('Digite o segundo numero inteiro: '))
if num > num2:
    print('O primeiro valor é maior')
elif num2 > num:
    print('O segundo valor é maior')
elif num == num2:
    print('Não existe valor maior, os dois são iguais.')