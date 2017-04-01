#!/usr/bin/python
import MySQLdb
from model import *

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="admin123",  # your password
                     db="mcdonalds")        # name of the data base
cur = db.cursor()

class FuncionarioController(object):

    @staticmethod
    def add(nome, senha, foto):

        func = Funcionario(nome, senha, foto)
        cur.execute("INSERT INTO funcionario (Nome, Senha, Foto, Privilegio) VALUES (%s, %s, %s, %s)", (func.nome, func.senha, func.foto, "0"))
        db.commit()

    @staticmethod
    def update(nome, n_nome, n_senha, n_foto, n_privilegio):

        funcID = cur.execute("SELECT * FROM funcionario WHERE Nome = (%s)", nome)
        cur.execute("UPDATE funcionario SET Nome = (%s) WHERE idFuncionario = (%s)", (n_nome, funcID))
        cur.execute("UPDATE funcionario SET Senha = (%s) WHERE idFuncionario = (%s)", (n_senha, funcID))
        cur.execute("UPDATE funcionario SET Foto = (%s) WHERE idFuncionario = (%s)", (n_foto, funcID))
        cur.execute("UPDATE funcionario SET Privilegio = (%s) WHERE idFuncionario = (%s)", (n_privilegio, funcID))
        db.commit()