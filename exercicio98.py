'''Função de Contador'''

from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('~~' * 20)
    print(f'Contagem de {inicio} até {fim} pulando de {passo} em {passo}.')

    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
            c += passo
        print('FIM!')
    else:
        c = inicio
        while c >= fim:
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
            c -= passo
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('~~' * 20)

print('Agora vem a sua personalização!')
i = int(input('Digite o número inicial da contagem: '))
f = int(input('Digite o número final da contagem: '))
p = int(input('Digite quantos números quer pular: '))

contador(i, f, p)
print('~~' * 20)
