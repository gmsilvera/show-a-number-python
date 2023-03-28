'''
# ESTRUTURAS CONDICIONAIS
# if else com and - ou seja, condição &
nome = "cynthia"
if 10 > 20 and nome == "cynthia":
    print("Olá, seja bem vinda")
else:
    print("você não é cynthia")

# if else com or - ou seja, condição OU
nome = "cynthia"
if 10 > 20 or nome == "cynthia":
    print("Olá, seja bem vinda")
else:
    print("você não é cynthia")

valor = 30
if valor > 200:
    print("Ok, valor maior que 200")
elif valor > 50:
    print("Ok, valor maior que 50")
elif valor > 40:
    print("Outra menssagem")5
else:
    print("Operação inválida!!!")

# for = interável, percorre cada indice
# Python For Loops

nomes = input("Digite seu nome.")
for l in nomes:
    print(l)

name = ['Laura', 'Lis', 'Guilherme', 'Enzo']
for nome in nomes:
    print(nome)

for i in [1, 2, 3, 4, 5]:
    print(f"Valor: {i}")
    print(i + 2)

# range - define o intervalo da interação
for item in range(3):
    print(item)

for item in range(2, 7):
    print(item)

for item in range(2, 9, 2):
    print(item)

'''

'''print("Digite duas notas do aluno")
notaUm = float(input("Insira uma nota: "))
notaDois = float(input("Insira a segunda nota: "))
media = (notaUm + notaDois)/2
print(media)
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")'''

print("Verifique se digitou M ou F")
opcao = str(input("Insira uma letra, de preferencia M ou F."))
letra = opcao
print(letra)

if letra == "M":
    print("Você digitou M, de sexo Masculino")
elif letra == "F":
    print("Você digitou F, de sexo Feminino")
else:
    print("Desculpe, Tente Novamente")
