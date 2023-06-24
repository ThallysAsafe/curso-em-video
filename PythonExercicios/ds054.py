from datetime import date
q = 0
z = date.today().year
for c in range(0,7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = z - ano
    if idade >= 18:
        q = q + 0
    else:
        q = q + 1
if q == 1:
    print('No total há {} pessoa que não atingiu a maior idade'.format(q))
elif q > 1:
    print('No total há {} pessoas que não atingiram a maior idade'.format(q))
else:
    print('Todos atingiram a maior idade')






