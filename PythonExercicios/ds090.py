dic = {}
nome = str(input('Nome: '))
media = float(input(f'Digite a média de {nome}:'))
dic['Nome'] = nome
dic['Média'] = media
if media >= 6:
    dic['Situação'] = 'Aprovado'
elif media >= 0:
    dic['Situação'] = 'Reprovado'
else:
    print('Valor inválido!')
    media = float(input(f'Digite a média de {nome}:'))
for k, v in dic.items():
    print(f'{k} é igual a {v} ')
