from datetime import date
ano = int(input('Qual é o seu ano de nascimento? '))
idade = date.today().year - ano
ft = 18 - idade
fts = idade - 18
if idade < 18 and ft > 1:
    print('Voce ainda vai se alistar ao serviço militar, falta ainda {} anos!'.format(ft))
elif idade < 18 and ft == 1:
    print('Voce ainda vai se alistar ao serviço militar, falta ainda {} ano!'.format(ft))
elif idade == 18:
    print('Está na hora de se alistar Amigão!')
elif idade > 18 and fts == 1:
    print('Passou do tempo do alistamento, ja passou {} ano!'.format(fts))
elif idade > 18 and fts > 1:
    print('Passou do tempo do alistamento, ja passou {} anos!'.format(fts))
