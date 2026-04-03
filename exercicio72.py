'''Número por Extenso'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número de 0 a 20: '))
while n < 0 or n > 20:
    print('Número inválido. Tente novamente.')
    n = int(input('Digite um número de 0 a 20: '))

print(f'Você digitou o número {extenso[n]}.')
