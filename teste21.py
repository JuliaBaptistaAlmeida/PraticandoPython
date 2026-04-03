'''Listas'''

lanche = ['pizza', 'hamburguer', 'suco', 'sorvete', 'bombom', 'pudim']
print(lanche)
lanche.append('cookie') #vai adicionar ao fim
lanche.insert(2, 'cachorro quente') #adiciona na posição 2
del lanche[0]
lanche.pop() #apaga o último
lanche.remove('sorvete')
lanche.sort() #põe em ordem
lanche.sort(reverse = True) #põe na ordem ao contrário
print(lanche)
