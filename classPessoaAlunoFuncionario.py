#ATIVIDADE PESSOA
'''Criar a classe Pessoa
a. Atributos: Nome, Endereço
b. Métodos: Alterar Nome, Endereço; Retornar Nome, Endereço.
Em seguida deve criar a classe Aluno que irá herdar os atributos
e métodos da classe Pessoa e a irá
acrescentar
a. Atributo: Nota
b. Métodos: Alterar e Retornar Nota
Considere, como subclasse da classe Pessoa a classe Fornecedor.

Considere que cada instância da classe Fornecedor tem, para além dos atributos que caracterizam a classe Pessoa, os atributos valorCredito (correspondente ao crédito máximo atribuído ao fornecedor) e valorDivida (montante da dívida para com o fornecedor).

Implemente na classe Fornecedor, para além dos usuais métodos seletores e modificadores, um método obterSaldo() que devolve a diferença entre os valores dos atributos valorCredito e valorDivida.

Depois de implementada a classe Fornecedor, crie um programa de teste adequado que lhe permita verificar o funcionamento dos métodos implementados na classe Fornecedor e os herdados da classe Pessoa.'''

class Pessoa:
    def __init__(self, nome, endereco):
        #underscore privado escrito antes do atributo _nome
        self._nome = nome
        self._endereco = endereco
    
    #metodo getter
    @property
    def nome(self):
        return self._nome
    
    #metodo setter
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    #novo_endereco é uma nova variável, não faz parte do contruct
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco
    
class Aluno(Pessoa):
    def __init__(self, nome, endereco, nota):
        super().__init__(nome, endereco)
        self._nota = nota

    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, nova_nota):
        self._nota = nova_nota

class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, valorCredito, valorDivida):
        super().__init__(nome, endereco)
        self._valorCredito = valorCredito
        self._valorDivida = valorDivida

    @property
    def valorCredito(self):
        return self.valorCredito

    @valorCredito.setter
    def valorCredito(self, novo_valorCredito):
        self.valorCredito = novo_valorCredito
    
    @property
    def valorDivida(self):
        return self.valorDivida

    @valorDivida.setter
    def valorDivida(self, novo_valorDivida):
        self.valorDivida = novo_valorDivida

    def obterSaldo(self, saldo):
        return self._valorCredito - self._valorDivida
        

aluno = Aluno('GEDERSON', 'PARAISO', 9)
print(aluno.nome)

fornecedor = Fornecedor(15000, 10000)
print(fornecedor.obterSaldo)
