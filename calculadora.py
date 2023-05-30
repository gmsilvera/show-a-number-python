from tkinter import *
import sys


class Calculadora:
    def __init__(self, janela):
        janela.title('Calculadora')
        janela.geometry("500x200")

        Label(janela, text='Valor 1 : ', width=8).pack(side=LEFT)
        self.valor1 = Entry(janela, width=10)
        self.valor1.pack(side=LEFT)

        Label(janela, text='Valor 2 : ', width=8).pack(side=LEFT)
        self.valor2 = Entry(janela, width=10)
        self.valor2.pack(side=LEFT)

        Label(janela, text=' = ', width=8).pack(side=LEFT)
        self.msg = Entry(janela, width=10)
        self.msg.pack(side=LEFT)

        somar1 = Button(janela, text='+', width=8, command=self.somar).pack()
        sutrair1 = Button(janela, text='-', width=8,
                          command=self.subtrair).pack()
        multiplicar1 = Button(janela, text='*', width=8,
                              command=self.multiplicar).pack()
        dividir1 = Button(janela, text='/', width=8,
                          command=self.dividir).pack()
        limpar1 = Button(janela, text='limpar', width=8,
                         command=self.limpar).pack()
        sair1 = Button(janela, text='sair', width=8, command=self.sair).pack()

    def somar(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        c = valor1 + valor2
        c = float(c)
        self.msg['text'] = '%f' % (c)

    def subtrair(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        c = valor1 - valor2
        c = float(c)
        self.msg['text'] = '%f' % (c)

    def multiplicar(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        c = valor1 * valor2
        c = float(c)
        self.msg['text'] = '%f' % (c)

    def divisao(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        c = valor1 / valor2
        c = float(c)
        self.msg['text'] = '%f' % (c)

    def limpar(self):
        self.valor1.delete(0, END)
        self.valor2.delete(0, END)
        self.msg['text'] = ""

    def sair(self):
        sys.exit()


app = Tk()
Calculadora(app)
app.mainloop()
