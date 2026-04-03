'''Par ou Ímpar?'''

from random import randint

print('PAR OU ÍMPAR?')
print('=-' * 8)
print('''Bem vindo(a)! Faça suas escolhas e veja suas vitórias no final. 
O jogo encerra quando você PERDER.''')
print ('=-' * 25)

vitorias = resultado = 0
while True:
    pi = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
    while pi not in 'PI':
        pi = input('Opção inválida! Escolha Par ou Ímpar [P/I]: ').strip().upper()[0]
    n = int(input('Digite seu número escolhido (0 a 10): '))
    while n < 0 or n > 10:
        n = int(input('Número inválido! Digite um número entre 0 e 10: '))
    computador = randint(0, 10)
    soma = computador + n
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    print(f'''O computador jogou {computador} e você jogou {n}. A soma é {soma}.''')
    if pi == resultado:
        print('VOCÊ VENCEUUU!')
        vitorias += 1
    else:
        print('VOCÊ PERDEU! O jogo será ENCERRADO.')
        break
print(f'Você obteve {vitorias} vitória(s). FIM DO PROGRAMA!')
