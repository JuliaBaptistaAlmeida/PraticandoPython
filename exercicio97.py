'''Um Print Especial'''

def escreva(frase):
    print('~' * len(frase))
    print(frase)
    print('~' * len(frase))

#Programa Principal
while True:
    texto = str(input('Digite uma frase: '))
    escreva(texto)
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Dados inválidos. Digite S para sim ou N para não: '))
        if continuar == 'N':
            break
