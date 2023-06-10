v = float(input('Qual foi a velocidade que o seu carro estava? '))
v2 = (v - 80) * 7
if v > 80:
    print('MULTADO! você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar a multa no valor de {} R$'.format(v2))
print('Tenha um bom dia, dirija com segurança!')
