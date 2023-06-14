a = float(input('Digite sua primeira nota: '))
b = float(input('Digite sua segunda nota: '))
c = (a + b) / 2
if c < 5:
    print('REPROVADO')
elif 5 >= c and c < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
