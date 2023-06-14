p = float(input('Digite o quanto você pesa: '))
h = float(input('Digite qual sua altura: '))
imc = p/h**2
if imc < 18.5:
    print('Abaixo do peso {:.2f} Kg/h'.format(imc))
elif imc >= 18.5 or imc <= 25:
    print('Peso Ideal {:.2f} Kg/h'.format(imc))
elif imc > 25 or imc <= 30:
    print('Sobrepeso {:.2f} Kg/h'.format(imc))
elif imc > 30 or imc <= 40:
    print('Obesidade {:.2f} Kg/h'.format(imc))
else:
    print('Obesidade mórbida {:.2f} Kg'.format(imc))
