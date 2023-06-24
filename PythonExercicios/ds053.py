print('Verificador de Palíndromo!')
frase = str(input('Digite uma frase palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('Você digitou a frase: {}'.format(palavras))
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é o {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('Não temos um palindromo!')
