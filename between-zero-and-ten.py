'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor Deseja
inválido e continue pedindo até que o usuário informe um valor válido'''

while True:
    valor_deintervalo = int (input("Digite uma nota entre zero e dez: \n"))
    if valor_deintervalo <= 10:
        print('Valor válido: ', valor_deintervalo)
        break
    else:
        print("Valor invalido, tente novamente.")