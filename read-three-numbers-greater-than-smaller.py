# Faça um Programa que leia três números e
# mostre o maior e o menor deles.
lista = []
qtd = 3
for i in range(qtd):
    elemento = int(input('Digite um numero: '))
    lista.append(elemento)

lista.sort(reverse=True)  # ordena os elementos
print(lista)
print(min(lista))
print(max(lista))
