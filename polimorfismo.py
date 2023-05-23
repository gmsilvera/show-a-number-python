'''POLIMORFISMO'''

class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        #underscore privado escrito antes do atributo _nome
        self._total_bonificacoes = total_bonificacoes
        
    def registra(self, funcionario):
        self.__total_bonificacoes += funcionario.get_bonificacao
    
    #decorador para retonar
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