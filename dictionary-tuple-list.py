'''Lista, Tuplas e Dicionário em Python'''

animais = [1, 2, 3, 4.5, "cachorro", "gato"]
print(type(animais))

animais[2] = "cachorro"
print(animais)

# Remover um índice da lista
animais.remove("cachorro")
print(animais)

# Inserção de valores na lista
animais.append("Cobra")
print(animais)
animais.insert(0, "Leão")
print(type(animais))

lista = [500, 30, 300, 80, 10]
print(lista)

# Ordenar a lista
lista.sort()
print(lista)

# Valor mínimo e máximo
print(min(lista))
print(max(lista))

''' # Lista aninhadas
listas = [["Cachorro, "Gato", "Cobra"],
          ["Fusca", "Ferrari", "Audi"],
          [10, 100, 200],
          ["Pedro", "Ana", 23]]

print(listas[3][2])'''

# Tuplas - usam pararênteses como sintaxe
tuplas = ("Banana", "Maçã", 10, 50)
print(type(tuplas))

# Tuplas são imutáveis!!! (importante)
# tuplas[0] = "Laranja"
# Contagem de indices
print(tuplas.count("Banana"))

# Dicionários
dicionario = {"Ana": 20, "João": 10, "Vitória": 15, "Paulo": 5}
print(dicionario["Ana"])

# Atualização de dicionários
dicionario["Ana"] = 30
print(dicionario)
# Remoção do indice no dicionário
dicionario.pop("Ana")
print(dicionario)
# Atualização do indice no dicionario
dicionario.update({"João": 10})
print(dicionario)
