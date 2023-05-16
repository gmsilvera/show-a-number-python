'''Python orientado a objeto'''

class Conta:
    '''construtor'''
    def __init__ (self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    '''metodos da classe CONTA'''
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        #self.saldo -= valor
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
        
    def gerarExtrato(self):
        print (f"numero: {self.numero}\n CPF: {self.cpf}\n saldo: {self.saldo}")


def main():
    ''''instancia da classe'''
    c1 = Conta(1,9000, "gederson", 1000)
    c1.depositar(300)
    saque = c1.sacar(400)
    c1.gerarExtrato()
    print(f"O saque foi realizado? {saque}")
    #print(f"Nome titular{c1.nomeTitular}")
    #print(f"CPF{C1.cpf}")

'''uso da classe'''
if __name__ == "___main__":
    main()