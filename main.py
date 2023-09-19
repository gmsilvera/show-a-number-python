from multiprocessing.dummy import current_process
from optparse import Values
import sqlite3
from model import Pessoa, Marca, Veiculo

banco = sqlite3.connect('database.db')
banco.execute("PRAGMA foreign_keys=on")
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa(
               cpf INTEGER PRIMARY KEY,
               nome TEXT NOT NULL,
               nascimento DATE NOT NULL,
               oculos BOOLEAN NOT NULL
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Marca(
               id INTEGER NOT NULL, 
               nome TEXT NOT NULL,
               sigla CHARACTER(2) NOT NULL,
               PRIMARY KEY(id)
);''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Veiculo(
               placa CHARACTER(7) NOT NULL,
               ano INTEGER NOT NULL,
               cor TEXT NOT NULL,
               proprietario INTEGER NOT NULL,
               marca INTEGER NOT NULL,
               PRIMARY KEY(placa),
               FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
               FOREIGN KEY(marca) REFERENCES Marca(id)
);''')
#cursor.execute('''ALTER TABLE Veiculo ADD motor REAL;''')
#pessoa = Pessoa(11122277733, 'Pedro', '2000-01-01', True)
#comando = '''INSERT INTO Pessoa(cpf, nome, nascimento, oculos) VALUES (?,?,?,?);'''
#cursor.execute(comando,(pessoa.cpf,pessoa.nome,pessoa.nascimento,pessoa.usa_oculos))
#banco.commit()

#INSERINDO POR LISTA DE VALORES
#pessoas = [Pessoa(11122233344, 'Joao', '2000-01-01', True), Pessoa(11122279733, 'Pedro', '2000-01-01', False)]
#comando = '''INSERT INTO Pessoa(cpf,nome,nascimento,oculos) VALUES (?,?,?,?);'''
#cursor.executemany(comando, [(i.cpf, i.nome, i.nascimento, i.usa_oculos) for i in pessoas])

#INSERINDO POR ESTRUTURA DE DICIONÁRIO
#pessoa = Pessoa(99955577744, 'Manu', '2000-01-01', True), Pessoa(77788899955, 'Jose', '2000-01-01', False)
#comando = '''INSERT INTO Pessoa(cpf, nome, nascimento, oculos) VALUES (:cpf,:nome,:nascimento,:usa_oculos);'''
#cursor.execute(comando,{"cpf":pessoa.cpf, "nome":pessoa.nome, "nascimento":pessoa.nascimento, "usa_oculos":pessoa.usa_oculos})

#pessoa = Pessoa(88855599944, 'Lara', '2000-01-01', False)
#comando = '''INSERT INTO Pessoa(cpf,nome,nascimento,oculos) VALUES (:cpf,:nome,:nascimento,:usa_oculos);'''
#cursor.execute(comando, vars(pessoa))
#print(vars(pessoa))

#marcaA =Marca("Marca A", "MA")
#comando = '''INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''
#cursor.execute(comando, vars(marcaA))
#marcaA.id = cursor.lastrowid

#marcaB =Marca("Marca B", "MB")
#cursor.execute(comando, vars(marcaB))
#marcaB.id = cursor.lastrowid

#comando2 = '''INSERT INTO Veiculo(placa,ano,cor,motor,proprietario,marca) #VALUES (:placa,:ano,:cor,:motor,:proprietario,:marca);'''
#veiculo1 = Veiculo("aaaaaaa", "2001", "prata", 1.0, 88855599944, marcaA.id)
#veiculo2 = Veiculo("bbbbbbb", "2000", "rosa", 2.0, 11122277733, marcaB.id)
#cursor.execute(comando2, vars(veiculo1))
#cursor.execute(comando2, vars(veiculo2))
#banco.commit()

#comando = '''UPDATE Pessoa SET oculos=:usa_oculos WHERE cpf=:cpf;'''
#cursor.execute(comando,{"usa_oculos": False, "cpf":88855599944})
#banco.commit()

#DELETAR UMA PESSOA DO BANCO DE DADOS
#comando = '''DELETE FROM Pessoa WHERE cpf=:cpf'''
#cursor.execute(comando,{"cpf":55566677755})
#banco.commit()

comando = ''''SELECT Veiculo.placa, Veiculo.ano, Veiculo.cor, Veiculo.motor, Veiculo.proprietario, Marca.nome from Veiculo JOIN Marca ON Marca.id = Veiculo.marca'''
cursor.execute(comando)
registros = cursor.fetchall()
print(registros)
banco.commit()

banco.closed()
