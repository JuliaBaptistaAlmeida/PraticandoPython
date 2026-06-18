# Declarando a classe Gafanhoto
class Gafanhoto:
    def __init__(self, n = "", i = 0): # Método construtor

        # Atributos de Instância
        self.nome = n
        self.idade = i

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    # Declaração de objetos
g1 = Gafanhoto("João", 20)
print(g1.mensagem())

print()
g2 = Gafanhoto("Maria", 25)
print(g2.mensagem())

print()
g1.aniversario()
print(g1.mensagem())

print()
g1.aniversario()
print(g1.mensagem())

print()
g2.aniversario()
print(g2.mensagem())