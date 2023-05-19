'''
Classe Bichinho Virtual:
Crie uma classe que modele um Tamagoshi (Bichinho Eletrônico):
a. Atributos: Nome, Fome, Saúde e Idade
b. Métodos: Alterar Nome, Fome, Saúde e Idade;
Retornar Nome, Fome, Saúde e Idade e imprimir
(deve apresentar os valores de todos os atributos)
Após a criação da classe, instancie dois Tamagoshis e
altere seus atributos e depois os imprima. 
'''


class Bichinho:

  def __init__(self, nome, fome, saude, idade):
    self.nome = nome
    self.fome = fome
    self.saude = saude
    self.idade = idade

  def alterarNome(self, nome):
    return nome

  def alterarFome(self, fome):
    return fome

  def alterarSaude(self, saude):
    return saude

  def alterarIdade(self, idade):
    return idade

  def imprimirAtributos(self):
    print(
      f"Nome do bichinho: {self.nome}\nEstá com fome: {self.fome}\nComo está sua saúde? {self.saude}\nQual a sua idade: {self.idade}\n"
    )


def main():
  T1 = Bichinho("Tamagoshi 01", "sim", "50%", "1 ano")
  T1.imprimirAtributos()

  print("---Tamagoshi 01 alterado---")
  nomeAlterado = T1.alterarNome("Tamagoshi 01.1")
  fomeAlterada = T1.alterarFome("Talvez")
  saudeAlterada = T1.alterarSaude("80%")
  idadeAlterada = T1.alterarIdade("2 anos")
  print(
    f"Nome do NOVO bichinho: {nomeAlterado}\nEstá com fome? {fomeAlterada}\nComo está sua saúde? {saudeAlterada}\nQual sua idade? {idadeAlterada}\n"
  )

  T2 = Bichinho("Tamagoshi 02", "não", "100%", "5 meses")
  T2.imprimirAtributos()

  print("---Tamagoshi 02 alterado---")
  nomeAlterado2 = T2.alterarNome("Tamagoshi 02.2")
  fomeAlterada2 = T2.alterarFome("Muita fome")
  saudeAlterada2 = T2.alterarSaude("30%")
  idadeAlterada2 = T2.alterarIdade("3 anos")
  print(
    f"Nome do NOVO bichinho: {nomeAlterado2}\nEstá com fome? {fomeAlterada2}\nComo está sua saúde? {saudeAlterada2}\nQual sua idade? {idadeAlterada2}\n"
  )

if __name__ == "__main__":
  main()
