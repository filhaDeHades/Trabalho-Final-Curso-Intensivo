import tkinter as tk
from Funcionario import Funcionario

class Mercado:
    def __init__(self, master=None):
        self.fonte = ('Bitstream Vera Sans', '15')

        self.login(master)
    
    def login(self, master):
        self.container1 = tk.Frame(master) #Nome
        #self.container1['pady'] = 15
        self.container1.pack()

        self.container2 = tk.Frame(master) #Senha
        self.container2['pady'] = 10
        self.container2.pack()

        self.container3 = tk.Frame(master) #Botao
        self.container3['pady'] = 5
        self.container3.pack()

        self.container4 = tk.Frame(master) #Mensagem de erro na entrada
        self.container4['height'] = 20
        self.container4.pack()

        self.label = tk.Label(self.container1, text='Login', font=('Bitstream Vera Sans', '16')
)
        self.label.pack()

        self.labelCodigo = tk.Label(self.container1, text='Código:', font=self.fonte)
        self.labelCodigo.pack(side='left')

        self.codigo = tk.Entry(self.container1, font=self.fonte)
        self.codigo.pack(side='left')

        self.labelSenha = tk.Label(self.container2, text='Senha:', font=self.fonte)
        self.labelSenha.pack(side='left')

        self.senha = tk.Entry(self.container2, font=self.fonte)
        self.senha['show'] = '*'
        self.senha.pack(side='left')

        self.entrar = tk.Button(self.container3, text='Entrar', font=self.fonte)
        self.entrar['command'] = self.verifica
        self.entrar.pack()

        self.labelMsg = tk.Label(self.container4, font=self.fonte)
        self.labelMsg.pack()
    
    def verifica(self):
        f = Funcionario()
        f.codigo = self.codigo.get()
        f.senha = self.senha.get()
        print(f'self.codigo = {self.codigo}')
        print(f'f.codigo = {f.codigo}')

        resp = f.verificaExiste()
        if resp == '1':
            self.labelMsg['text'] = resp
            self.menu()
        else:
            print('Não existe')
            self.labelMsg['text'] = resp
    
    def menu(self):
        pass

root = tk.Tk()
Mercado(root)
root.mainloop()