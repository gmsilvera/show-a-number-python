'''REVISÃO SOBRE FUNÇÃO EM PYTHON'''

'''função sem retorno'''
def mostrar_mensagem ():
    print ('Hello World')

for i in range (5):
    mostrar_mensagem ()



def assinar (nome, email):
    print ('atenciosamente')
    print ('Profe', nome)
    print ('Email', email)

assinar("gederson", "gederson@gmail.com")


'''função com retorno'''
def area_circulo (r):
    area = 3.14*r**2
    return area

a = area_circulo(2)
print ("area_circulo é", a)


'''função com input'''
def leitura_nome():
    pnome = input("Digite seu nome: ")
    snome = input("Digite também o seu sobrenome: ")
    nome = pnome + " " + snome
    return nome

usuario = leitura_nome()
print("O usuário: ", usuario)


'''atividade: calculo de imposto sobre um determinado produto'''
def somaImposto (taxaImposto, custo):
    imposto = custo + (custo*taxaImposto / 100)
    return imposto

imposto = float(input("digite a taxa do imposto: "))
custo = float(input("digite o valor do produto: "))
precoTotal = somaImposto(imposto, custo)

print("O custo final é: ", precoTotal)








