#Faça um Programa que peça a idade e a altura de 5 
# pessoas, armazene cada informação no seu
# respectivo vetor. Imprima a idade e a altura na
# ordem inversa a ordem lida. 

idade = []
altura = []

print("Digite sua idade e altura.")
for p in range(5):
    Pessoa = []
    print("Pessoa " + str(p + 1) + ": "  + " ")
    for i in range(1):
        idadesTotais = int(input("Idade " + str(i + 1) + ": "  + " "))
        idade.append(idadesTotais)
        for a in range(1):
            alturasTotais = float(input("altura " + str(a + 1) + ": "  + " "))
            altura.append(alturasTotais)

print("Ordem da lista")
print(idade)
print(altura)

idade.reverse()
altura.reverse()

print("Ordem inversa: ")
print(idade)
print(altura)