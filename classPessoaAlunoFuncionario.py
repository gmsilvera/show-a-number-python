class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def retornar_nome(self):
        return self.nome

    def retornar_endereco(self):
        return self.endereco


class Aluno(Pessoa):
    def __init__(self, nome, endereco, nota):
        super().__init__(nome, endereco)
        self.nota = nota

    def alterar_nota(self, nova_nota):
        self.nota = nova_nota

    def retornar_nota(self):
        return self.nota


class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, valor_credito, valor_divida):
        super().__init__(nome, endereco)
        self.valor_credito = valor_credito
        self.valor_divida = valor_divida

    def alterar_valor_credito(self, novo_valor_credito):
        self.valor_credito = novo_valor_credito

    def alterar_valor_divida(self, novo_valor_divida):
        self.valor_divida = novo_valor_divida

    def obter_saldo(self):
        return self.valor_credito - self.valor_divida


# Programa de teste
fornecedor = Fornecedor("SAMSUNG", "MANAUS", 10000, 3000)
print("\nDADOS inicial do FORNECEDOR: ", fornecedor.nome, fornecedor.endereco, fornecedor.valor_credito, fornecedor.valor_divida)
print("\n***DADOS DO FORNECEDOR***")
print("Nome:", fornecedor.retornar_nome())
print("Endereço:", fornecedor.retornar_endereco())
print("Saldo:", fornecedor.obter_saldo())

fornecedor.alterar_valor_credito(20000)
fornecedor.alterar_valor_divida(7000)

print("\nNOVOS DADOS", fornecedor.nome)
print("Nome:", fornecedor.retornar_nome())
print("Endereço:", fornecedor.retornar_endereco())
print("Saldo:", fornecedor.obter_saldo())

fornecedor2 = Fornecedor("HONDA", "FORTALEZA", 20000, 2000)
print("\nDADOS inicial do FORNECEDOR: ", fornecedor2.nome, fornecedor2.endereco, fornecedor2.valor_credito, fornecedor2.valor_divida)

print("\n***NOVO - DADOS DO FORNECEDOR***")
print("NOVO Nome:", fornecedor2.retornar_nome())
print("NOVO Endereço:", fornecedor2.retornar_endereco())
print("NOVO Saldo:", fornecedor2.obter_saldo())
print("\nSaldo atualizado:", fornecedor2.obter_saldo())

fornecedor2.alterar_valor_credito(30000)
fornecedor2.alterar_valor_divida(10000)

print("\nNOVOS DADOS", fornecedor2.nome)
print("\n***NOVO - DADOS DO FORNECEDOR***")
print("NOVO Nome:", fornecedor2.retornar_nome())
print("NOVO Endereço:", fornecedor2.retornar_endereco())
print("NOVO Saldo:", fornecedor2.obter_saldo())
print("\nSaldo atualizado:", fornecedor2.obter_saldo())
