from datetime import date
nasc = int(input('Digite o seu ano de nascimento: '))
ida = date.today().year - nasc
if ida <= 9:
    print('Você pertence a categoria MIRIM!')
elif ida <= 14:
    print('Você pertence a categoria INFANTIL!')
elif ida <= 19:
    print('Você pertence a categoria JUNIOR!')
elif ida <= 20:
    print('Você pertecnce a categoria SÊNIOR!')
else:
    print('Você pertence a categoria MASTER!')
