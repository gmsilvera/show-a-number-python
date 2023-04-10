'''
Utilizando listas implemente um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". '''

print("\nPreciso que responda 5 perguntas sobre um crime.\n")

perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

lista_resposta = []

for i in perguntas:
    print(i)
    resposta = input("Digite sim ou não: ")
    if "sim" or "não" in resposta:
        lista_resposta.append(resposta)
       
print(lista_resposta)

print("Classificação sobre a participação da pessoa no crime.")

if lista_resposta.count("sim") == 2:
    print("Suspeita")
elif lista_resposta.count("sim") == 3 or lista_resposta.count("sim") == 4:
    print("Cúmplice")
elif lista_resposta.count("sim") == 5:
    print("Assassino")
else:
    print("Inocente")


