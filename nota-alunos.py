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

file = open("new-file.txt", "r")

try:
    file.read()
except FileExistsError:
    print("not found")

file.close()

try:
    open(file, "w")
    print("here")
except IOError:
    print("write impossible")

#criar o ambiente virtual python -m venv env
#-\env\Scripts\activate
#INSTALAR OS PACOTES SOMENTE DEPOIS DA ATIVAÇAO
#desativar deactivate
####LINUX -\env\bin\activate
#-\env\Scripts\activate
