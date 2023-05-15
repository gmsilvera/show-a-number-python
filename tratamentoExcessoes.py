'''Tratamento de excessoes - try except'''

try:
    num = eval(input("Digite um número: "))
    print(num)
except:
    print("Valor incorreto. Digite um número.")
    
    
try:
    num = eval(input("Entre com um valor: "))
    resut = 10/num
    
except ZeroDivisionError as e:
    print("Não é possível dividir por zero", e)
except NameError as e:
    print("Não é um número", e)
    