# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
media = []
for n in range(4):
    soma = 0
    nota = float(input("Notas" + str(n + 1) + ": "))
    notas.append(nota)
    for s in notas:
        soma += s

print("Total da soma: ", soma)
media = soma / 4

print("Notas: ", notas)
print("media: ", media)