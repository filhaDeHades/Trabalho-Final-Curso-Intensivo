from Banco import Banco

class Funcionario:
    def __init__(self):
        self.nome = None
        self.codigo = '0000000000'
        self.senha = None
    
    def addAoBanco(self):
        banco = Banco()

        try:
            c = banco.conecta.cursor()

            c.execute('INSERT INTO funcionario(nome, codigo, senha) VALUES (?, ?, ?)',(self.nome, self.codigo, self.senha))
            banco.conecta.commit()
            c.close()

            return('Funcionário Cadastrado')
        except:
            return('Não foi possível cadastrar o funcionário')
    
    def verificaExiste(self):
        banco = Banco()

        try:
            c = banco.conecta.cursor()

            c.execute('SELECT * FROM funcionario WHERE codigo = ?', (self.codigo, ))
            row = c.fetchone()
            print(f'Row = {row}')
            if row == None:
                return ('Usuário ou senha não encontrados')
            else:
                self.nome = row[1]
                return('1')
                
        except:
            pass