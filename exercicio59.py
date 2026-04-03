'''Menu de Opções'''

from time import sleep
num1 = int (input('Digite o primeiro número: '))
num2 = int (input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    print ('''O que deseja fazer?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    escolha = int (input('Selecione a opção desejada: '))
    if escolha == 1:
        soma = num1 + num2
        print (f'A soma de {num1} e {num2} é igual a {soma}.')
    elif escolha == 2:
        x = num1 * num2
        print (f'O resultado de {num1} X {num2} é igual a {x}.')
    elif escolha == 3:
        if num1 > num2:
            maior = num1
            print (f'O maior número entre {num1} e {num2} é {maior}.')
        elif num2 > num1:
            maior = num2
            print (f'O maior número entre {num1} e {num2} é {maior}.')
        else:
            print ('Os dois números são iguais.')
    elif escolha == 4:
        print ('Informe os novos números...')
        num1 = int (input('Digite o primeiro número: '))
        num2 = int (input('Digite o segundo número: '))
    elif escolha == 5:
        print ('Finalizando...')
    else:
        print ('Opção inválida. Tente novamente.')
    print ('=-' * 15)
    sleep (2)
print ('Programa encerrado. Até breve!')
    