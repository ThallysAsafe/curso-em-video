print("Tabela do Campeonato Brasileiro de Futebol")
tabela = ('Botafogo', 'Flamengo', 'Grêmio', 'São Paulo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Athletico-PR')
tabela2 = ('Fortaleza', 'Cruzeiro', 'Internacional', 'Atlético-MG', 'Cuiabá', 'Santos', 'Corinthians', 'Bahia', 'Goiás')
tabela3 = ('Coritiba', 'Vasco', 'América-MG')
total = tabela + tabela2 + tabela3
print(f'Tabela dos times no Brasileirão: {total}')
# Letra A
print(f'Tabela do Campeonato Brasileiro dos Cinco Primeiros Colocados: {tabela[0:6]}')
# Letra B
print(f'Tabela do Campeonato Brasileiro de Futebol dos Quatro Ultimos colocados: {total[17:20]}')
# Letra C
print(f'Tabela do Campeonato Brasileiro de Futebol em Ordem Alfabética: {sorted(total)}')
# Letra D
n = total.index('Flamengo')
n += 1
print(f'A posição do Flamengo na Tabela: {n}º')
