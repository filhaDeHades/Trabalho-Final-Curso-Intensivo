import sqlite3 as slite

class Banco():
    def __init__(self):
        self.conecta = slite.connect('banco.db')
        self.row_factory = slite.Row
        self.createFuncionario()
    
    def createFuncionario(self):
        c = self.conecta.cursor()

        c.execute('''
        CREATE TABLE IF NOT EXISTS funcionario(
            codigo VARCHAR(10) PRIMARY KEY,
            nome VARCHAR(40) NOT NULL,
            senha VARCHAR(8) NOT NULL
        );
        ''')
        c.execute('SELECT * FROM funcionario WHERE codigo = "0100000001"')
        row = c.fetchone
        if not row:
            c.execute('INSERT INTO funcionario(nome, codigo, senha) VALUES ("adm", "0100000001", "senha")')
        self.conecta.commit()
        c.close()
    
    def createProduto(self):
        c = self.conecta.cursor()

        c.execute('''
        CREATE TABLE IF NOT EXISTS produto(
            codigo VARCHAR(10) PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            preco DOUBLE NOT NULL,
        );
        ''')
        self.conecta.commit()
        c.close()
