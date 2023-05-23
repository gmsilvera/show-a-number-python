class Pessoa():
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
        self._endereco = novo_nome
    
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    #novo_endereco é uma nova variável, não faz parte do contruct
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco
    
class Aluno(Pessoa):
    def __init__ (self, nome, endereco, nota):
        super().__init__(nome, endereco)
        self._nota = nota

    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nome(self, nova_nota):
        self._nota = nova_nota
