'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).'''
print('Converter a temperatura Fahrenheit para Celsius')
temperaturaFahrenheit = float(input('Digite o valor da temperatura em Fahrenheit: '))

temperaturaEmCelsius = 5*((temperaturaFahrenheit-32)/9)

print('O valor da temperatura em Celsius é {}.'.format(temperaturaEmCelsius))