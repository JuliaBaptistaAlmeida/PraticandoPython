'''Tuplas'''

lanche = ('pizza', 'hamburguer', 'suco', 'pudim')
print(lanche[1:3])

lanche = ('pizza', 'hamburguer', 'suco', 'pudim')
print(lanche[2:])

lanche = ('pizza', 'hamburguer', 'suco', 'pudim')
print(lanche[:3])

lanche = ('pizza', 'hamburguer', 'suco', 'pudim')
print(sorted(lanche)) #ordem alfabética

lanche = ('pizza', 'hamburguer', 'suco', 'pudim')
print(lanche.index('suco')) #fala a posição do suco

lanche = ('pizza', 'hamburguer', 'suco', 'pudim')
print(len(lanche))

lanche = ('pizza', 'hamburguer', 'suco', 'pudim', 'pizza')
print(lanche.count('pizza')) #conta quantas vezes aparece

lanche = ('pizza', 'hamburguer', 'suco', 'pudim', 'pizza')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
