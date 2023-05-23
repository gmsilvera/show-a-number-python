'''forma incorreta'''
'''
class Funcionario:
    def __init__ (self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    
class Gerente:
    def __init__ (self, nome, cpf, salario, senha, qnt_gerenciados):
        self.nome = nome
        self.cpf = cpf
        self.sasalario = salario
        self.senha = senha
        self.qnt_gerencia = qnt_gerenciados
'''

'''Herânça correta - atributos, metodos'''
class Funcionario:
    def __init__ (self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10

class Gerente(Funcionario):
    def __init__ (self, nome, cpf, salario, senha, qnt_gerenciados):
        super().__init__(nome, cpf, salario)
        #super usado para referenciar a class mãe(Funcionario)
        self.senha = senha
        self.qnt_gerencia = qnt_gerenciados
    
    def autentica(self, senha):
        if self._senha == senha:
            print('Acesso permitido')
        else:
            return False
    
    def get_bonificacao(self):
        return self._salario * 0.15

gerente = Gerente('Jose'. '22222', 5000.0, '1234', 0)
print(gerente.get_bonificacao())

class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes
        
    def registra(self, funcionario):
        self.__total_bonificacoes += funcionario.get_bonificacao
    
    @property
    def total_bonificacoes(self):
        return self ._total_bonificacoes
    
if __name__ == '__main__':
    funcionario = Funcionario('Joao', '111111', 2000.0)
    print("bonificacao funcionario: {}".format(funcionario.get_bonificacao))
    
    gerente = Gerente('Jose', '222222', 5000, '123465'. )
    print("bonificacao gerente: {}".format(gerente.get_bonificacao))

    controle = ControleDeBonificacoes()
    controle.registra(funcionario)
    controle.registra(gerente)
    
    print('total: {}'.format(controle.total_bonificacoes))