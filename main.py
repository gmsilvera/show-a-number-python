from multiprocessing.dummy import current_process
import sqlite3
# primeiro conectar, observação: sempre formato o .db
banco = sqlite3.connect('database.db')
# para que consiga enviar dados para o bando
cursor = banco.cursor()

# criar tablea com nome de cada coluna
cursor.execute("CREATE TABLE IF NOT EXISTS cliente(nome text, idade integer, sex text)")

# inserção de valores
cursor.execute("INSERT INTO cliente VALUES ('Cynthia', 40, 'F'), ('Pedro', 20, 'M')")

banco.commit()
cursor.execute("Select * from cliente")
#fetchall recupera todos os registro da consulta
print(cursor.fetchall())

# fechar o cursor e fechar o banco
cursor.close()
banco.close()


