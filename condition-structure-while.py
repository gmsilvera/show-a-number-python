'''
print ('Hello World')

palavra = input("Entre com uma palavra: \n")
while palavra != 'sair':
    palavra  = input('Digite sair para encerrar o laço.')
print('Você digitou sair e agora está fora do laço.')
'''

'''
while True:
    palavra = input("Entre com uma palavra: \n")
    if palavra == 'sair':
        break #INTERROMPE AS REPETIÇÕES DOS LAÇOS
print('Você digitou sair e agora esta fora do laço.')
'''

'''
while True:
    print ('Você esta no primeiro laco.')
    opcao1 = input("Deseja sair dele? Digitie SIM: \n")
    if opcao1 == 'SIM':
        break #INTERROMPE AS REPETIÇÕES DOS LAÇOS
    else:
        while True:
            print ('Você esta no segundo laco.')
            opcao2 = input('Deseja sair dele, digite SIM \n' )
            if opcao2 == 'SIM':
                break #INTERROMPE AS REPETIÇÕES DOS LAÇOS
        print('Você saiu do segundo laco.')
print('Você saiu do primeiro laco.')
'''

'''
#range EXEMPLO: Crie uma sequência de números de 0 a 5 e imprima cada item na sequência:
for num in range(1, 11):
    if num == 5:
        continue #pula uma iteração do loop
    else:
        print(num)
print('Laco encerrado!')
'''

'''
#VERIFICAR SE O NÚMERO E PAR OU ÍMPA
for num in range(1, 11):
    if num % 2 == 0: #VERIFICA SE O RESTO DA DIVISÃO E IGUAL A 0 (ZERO)
        pass
    else:
        print(num)
print('Laco encerrado!')
'''

'''
escolha = input("Escolha uma opcao de funcao: 1 OU 2")

if escolha == "1":
    def func1(x):
        return x + 1
        s = fun1(10)
else:
    def func2(x):
        return x + 2
        s = funcao(10)

print(s)
'''

'''
def taximetro(distancia, multiplicador=1):
    largada = 3
    km_rodado = 2
    valor = (largada + (distancia *km_rodado)) * multiplicador
    return  valor
    
pagamento = taximetro(3.5)

print(pagamento)
'''

''' exemplo de variáveis globais e locais
def func1(x):
    x = 10 #VARIAVEL LOCAL
    print(f'Funcao func1 - x = {x}')
    
def func2(x):
    x = 20 #VARIAVEL LOCAL
    print(f'Funcao func2 - x = {x}')
    
x=0 #VARIAVEL GLOBAL
func1(x)
func2(x)
print(f'Programa principal - x = {x}')
'''

'''
def func1():
    global x
    x = 10 #VARIAVEL LOCAL
    print(f'Funcao func1 - x = {x}')
    
def func2():
    global x
    x = 20 #VARIAVEL LOCAL
    print(f'Funcao func2 - x = {x}')
    
x=0 #VARIAVEL GLOBAL
func1()
func2()
print(f'Programa principal - x = {x}')


#função recursiva, chama a si mesmo
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1)
        
print(fatorial(5))
'''

'''
def result(func1, func2, fatorial):
print('result' + result())
'''

def regressiva(x): #chama a si mesmo
    if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva(x-1)

print(regressiva(4))

