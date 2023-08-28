
#CAMINHA ABSOLUTO
'''arquivo = open("C:\\Users\\201902472063\\Documents\\aula03", "r")

print(arquivo)
'''
"""
#CAMINHO RELATIVO
arquivo = open("test.txt", "r",encoding="UTF-8")

#retornar o cursor no caractere especifico
print(arquivo.seek(0))
#read leitura do arquivo / ABERTURA DE ARQUIVO
print(arquivo.read())
#aparecer a primeira linha
print(arquivo.readline())
#abrir o aquivo e fechar
arquivo.close()
print(arquivo.closed)

arquivo = open("novo.txt","w")
print(arquivo)
arquivo.write("Arquivo de escrita")
arquivo.close()
print(arquivo.closed)
"""
'''
from asyncore import write


arquivo = open("frutas.txt","w")
arquivo.write("banana" + "\n")
arquivo.write("uva" + "\n")
arquivo.write("mamao" + "\n")

arquivo.close()

arquivo = open("frutas.txt","r")
print(arquivo.read())
arquivo.close()

#loop para inclusão automatica de dados no arquivo
precos = [100,200,500,1000]
with open("precos.txt","w") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + "\n")
print(arquivo.closed)

#uso do append incluindo no arquivo
#OBSERVAÇÃO, o w SOBRESCREVE O ARQUIVO, uso correto e o append
precos = [5000]
with open("precos.txt","a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + "\n")
print(arquivo.closed)

precos = [5000]
with open("precos.txt","a") as arquivo:
    for preco in precos:
        arquivo.write('60000' + '\n')
print(arquivo.closed)

#LEITURA COM WITH
with open("precos.txt","r") as arquivo:
    print(arquivo.read())

arquivo = open("musicas.txt","a")
tipos = ['rock\n', 'forro\n']
arquivo.writelines(tipos)

arquivo = open("musicas.txt","r")
print(arquivo.read())

disciplinas = ["\nrad\n", "so\n", "web\n"]
with open ("disciplinas.txt","w", encoding="UTF-8") as file:
    file.write("relação de disciplinas")
    file.writelines(disciplinas)


#não e possível
with open("novo.txt", "r+") as file2:
        print(file2.read())

'''

alunos = [{"cynthia", 5, 10}, {"julio", 4, 10}, {"isa", 5, 7}]

with open("notas.txt", "w") as arquivo:
    arquivo.write("NOTAS DE 3 ALUNOS")
    for aluno in alunos:
            nome = aluno[0]
            av1 = aluno[1]
            av2 = aluno[2]
            media = (av1+av2)/2
            arquivo.write("\n" + str(aluno) + "\n")
            arquivo.write(f"{nome}, {av1}, {av2}, {media} \n")
    

with open("notas.txt", 'r') as arquivo:
    print(arquivo.read())

