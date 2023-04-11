# Faça um programa que leia um vetor de 5 números inteiros e mostre-os.
# listas podem ser utilizadas na representação de vetores.
'''
Numeros = []
print("Informe 5 números")
for i in range(5):
    Numeros.append(input("Informe o número" + ":\n"))
    print(Numeros)

# Faça um programa que peça as quatro notas 10 de uma quantidade de determinada de alunos,
# calcule sua média por aluno e informe a quatidade de aprovados.

Notas = []
print("NOTAS DOS ALUNOS")

#interar 10 alunos
for i in range(2):
    # print(i)
    soma = 0
    Aluno = []
    print("Aluno: " + str(i + 1)) #Aluno: 1
    
    #interar 4 notas para cada aluno
    for j in range(4):
        nota = float(input("Nota " + str(j + 1) + ":\n"))
        while nota < 0 or nota > 10:
            print("Nota inválida. Digite um valor válido")
            nota = float(input("Nota " + str(j + 1) + ': '))
        Aluno.append(nota)
        soma += Aluno[j]
    
    #media para cada aluno
    media = soma / 4
    Notas.append(media)

#exibir a quantidade de alunos aprovados
aprovados = 0
for nota in Notas:
    if nota >= 7.0:
        aprovados += 1
print('Números de alunos aprovados: ', aprovados)'''


#Faça um programa que leia duas strings,
#informe se as duas strings possuem o mesmo comprimento e são iguais
'''
palavra1 = input("Digite a primeira palavra: ")
print = input("A primeira palavra foi: " + palavra1 + '\n' + "Seu tamanho é: " + str(len(palavra1)))

palavra2 = input("Digite a segunda palavra: ")
print = input("A segunda palavra foi: " + palavra2 + '\n' + "Seu tamanho é: " + str(len(palavra2)))

if len(palavra1) == len(palavra2):
    if palavra1 == palavra2:
        print("As duas palavras são iguais e têm o mesmo tamanho.")
    else:
        print("As duas palavras são diferentes, mas o mesmo tamanho.")
else:
    print("As duas palavras são diferentes.")'''


#informe 20 números e indentifique e liste os números, os números pares e impares
'''
lista_impa = []
lista_par = []
listaNumeros = []
numero = 0
print('Informe os números: ')
for i in range(3):
    listaNumeros.append((int(input('Números: ' + str(i+1) + "\n"))))
    numero = listaNumeros[i]
    #print(numero)
    if(numero%2 ==0):
        lista_par.append(numero)
    else:
        lista_impa.append(numero)

print("Lista de números: " + listaNumeros)
print("Lista de números pares: " + lista_par)
print("Lista de números impares: " + lista_impa)

##Matrizes
#Calcular a media de 3 turmas
turma = [[5.0, 4.5, 7.0, 5.2, 6.1], [2.1, 6.5, 8.0, 7.0, 6.7], [8.6, 7.0, 9.1, 8.7, 9.3]]
#print(turma[0][1])
#print(turma[2][4])
#Calcula a média
media = 0

'''

#For para percorrer as linhas
'''
for i in range(3):
    #for para percorrer as colunas
    for j in range(5):
        media = media + turma[i][j]
    media = media / len(turma[i])
    print(media)
'''

#inserir dados nas linhas e colunas de uma matriz com 3 linhas e 3 colunas
'''
turma = []
for i in range(2):
    #cria a linha vazia
    linha = []
    for j in range(3):
        #vai adicionando as notas na linha
        linha.append(int(input('Digite a nota[' + str(i) + ',' + str(j) + ']:')))
    #adiciona a linha na matriz turma
    turma.append(linha)

'''


idade = []
altura = []
listaPessoasComIdade = []
pessoasIdade = []
listaPessoasComAltura = []
pessoasAltura = []
print("Idade e altura")
for i in range(5):
    # print(i)
    idade.append((int(input('Idade: ' + str(i+1) + " "))))
    pessoasIdade = listaPessoasComIdade[i]
    for a in range(5):
        altura.append((int(input('Altura: ' + str(a+1) + " "))))
        pessoasAltura = listaPessoasComAltura[a]
    
    print(pessoasIdade)
    print(pessoasAltura)

