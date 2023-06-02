from tkinter import *
import sys
from math import cos, sin, sqrt, tan
import math

class Calculadora:
    def __init__(self, janela):
        janela.title('Calculadora')
        janela.geometry("500x200")

        Label(janela, text='Valor1 :', width=8).pack(side=LEFT)
        self.valor1 = Entry(janela, width=10)
        self.valor1.pack(side=LEFT)

        Label(janela, text='Valor2 :', width=8).pack(side=LEFT)
        self.valor2 = Entry(janela, width=10)
        self.valor2.pack(side=LEFT)

        Label(janela, text=' = ', width=8).pack(side=LEFT)
        self.msg = Label(janela, width=10)
        self.msg.pack(side=LEFT)

        buttonSomar = Button(janela, text='+', width=8, command=self.somar).pack()
        buttonSubtrair = Button(janela, text='-', width=8, command=self.subtrair).pack()
        buttonMultiplicar = Button(janela, text='*', width=8,command=self.multiplicar).pack()
        buttonDividir = Button(janela, text='/', width=8, command=self.dividir).pack()
        buttonSeno = Button(janela, text='sin', width=8, command=self.seno).pack()
        buttonCoseno = Button(janela, text='cos', width=8, command=self.coseno).pack()
        
        limpar = Button(janela, text='limpar', width=8,command=self.limpar)
        limpar.pack()

        sair = Button(janela, text='sair', width=8, command=self.sair).pack()

    def somar(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        self.msg['text'] = '%f' % (valor1 + valor2)

    def subtrair(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        self.msg['text'] = '%f' % (valor1 - valor2)

    def multiplicar(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        self.msg['text'] = '%f' % (valor1 * valor2)

    def dividir(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        self.msg['text'] = '%f' % (valor1 / valor2)

    def seno(self):
        valor1 = float(self.valor1.get())
        self.msg['text'] = '%f' % (sin(valor1))

    def coseno(self):
        valor1 = float(self.valor1.get())
        self.msg['text'] = '%f' % (cos(valor1))


    def limpar(self):
        self.valor1.delete(0, END)
        self.valor2.delete(0, END)
        self.msg['text'] = ""

    def sair(self):
        sys.exit()


app = Tk()
Calculadora(app)
app.mainloop()
