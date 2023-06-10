from datetime import date
ano = int(input('Escolha um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[1;29;40m{}\033[m é um ano bissexto'.format(ano))
else:
    print('O ano \033[1;29;40m{}\033[m não é um ano bissexto'.format(ano))
