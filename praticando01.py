"Vogais"

vogais = 0

print()
palavra = str(input("Digite uma palavra: "))

for letra in palavra:
    maiuscula = letra.upper()
    if maiuscula in 'AEIOU':
        vogais += 1

print()
print(f"Sua palavra tem {vogais} vogais.")
print()

#quando é str, o for roda letra por letra
