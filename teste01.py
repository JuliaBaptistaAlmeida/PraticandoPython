'''Lista ao Contrário'''

lista = []

while True:
    print()
    nomes = str(input("Digite um nome para adicionar à lista: "))
    lista.append(nomes)
    print()
    
    continuar = str(input("Deseja continuar? [S/N]: ")).upper().strip()
    if continuar not in 'SN':
        print()
        continuar = str(input("Digite S para sim ou N para não: ")).upper().strip()
    if continuar == 'N':
        print()
        print("Aqui está a lista ao contrário:")
        lista.reverse()
        print(lista)
        break
    
print("FIM DO PROGRAMA!")
