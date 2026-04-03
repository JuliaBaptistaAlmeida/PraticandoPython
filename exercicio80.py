'''Lista Ordenada, Sem Repetições'''
#colocando em ordem sem usar o sort()

lista= []

for c in range(0,5):
    n = int(input('Digite um valor: '))

    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posção {pos} da lista')
                break
            pos += 1

print(f'Os valores da lista em ordem crescente são: {lista}')
