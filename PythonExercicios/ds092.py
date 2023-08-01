from datetime import date
perfil = {'Nome': str(input('Nome: '))}
anodenasc = int(input('Ano de Nascimento: '))
perfil['idade'] = date.today().year - anodenasc
perfil['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if perfil['Carteira de Trabalho'] > 0:
    perfil['Ano de Contratação'] = int(input('Ano de Contratação: '))
    perfil['Salário'] = float(input('Salário: '))
    perfil['Aposentadoria'] = (perfil['Ano de Contratação'] - anodenasc) + 35
    for k, v in perfil.items():
        print(f'{k} tem valor {v}')
elif perfil['Carteira de Trabalho'] == 0:
    for k, v in perfil.items():
        print(f'{k} tem valor {v}')
