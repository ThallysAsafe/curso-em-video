print('Progressão aritimética')
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = t + (10-1) * r
for c in range(t, d + r, r):
    print(c, end=' ')
