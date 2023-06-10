sal = float(input('Digite o valor do seu salário: '))
if sal > 1250:
    print('Seu salario sofreu um aumento de 10%, agora o valor dele é {}R$ '.format(sal + (sal * 10/100)))
else:
    print('Seu salario sofreu um aumento de 15%, agora o valor dele é {}R$'.format(sal + (sal * 15/100)))


