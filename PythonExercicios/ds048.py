s = 0
count = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        print(c)
        count += 1
        s += c
print('A Soma de todos os {} valores solicitados, mutiplos de 3 é igual a {}'.format(count, s))
