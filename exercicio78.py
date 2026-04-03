'''Menor e Maior em Listas'''
#min e max

pos = 0
lista = []

for n in range(0,5):
    n = int(input(f'Digite um valor para a posição {pos}: '))
    pos += 1
    lista.append(n)
    
    menor = min(lista)
    maior = max(lista)

print(f'Você digitou {lista}.')

print(f'O menor valor foi {menor}, na posição ', end='')
for posicao, numero in enumerate(lista):
    if numero == menor:
        print(f'{posicao}, ', end='')
print(f'O maior valor foi {maior}, na posição ', end='')
for posicao, numero in enumerate(lista): #poderia ser i(indice) ou v(valor).
    if numero == maior:
        print(f'{posicao}, ', end='')

#indice:posiçao dos numeros
#valor:os numeros em si