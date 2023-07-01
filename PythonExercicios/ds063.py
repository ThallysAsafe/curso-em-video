import math
n = int(input('Digite quantos elementos você quer que apareça: '))
x = 0
a = 1
b = 1
while x != n:
    x += 1
    r = b
    if x > 2:
        a = a + b + r
        r += 1
    print(a)

