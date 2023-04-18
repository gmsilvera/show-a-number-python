from math import cos, sin, sqrt, tan
import math

print("CALCULADORA BÁSICA\n")
numero1 = eval(input("Digite um número: "))
numero2 = eval(input("Digite o segundo número: "))

opcao = float(input("\nEscolha a operação desejada: \n0 -Raiz quadrada. \n1 -Potenciação. \n2 -Seno. \n3 -Cosseno. \n4 -Tangente. \n"))

if opcao == 0:
    print ("A raiz quadrada é: ", sqrt(numero1))

if opcao == 1:
    print ("O Potenciação é: ", (numero1 ** numero2))

if opcao == 2:
    print ("O seno é: ", sin(numero1))
    
if opcao == 3:
    print ("O cosseno é: ", cos(numero1))

if opcao == 4:
    print ("O tangente é: ", tan(numero1))
