def menu(l):
	print('\033[033m\nEsse é o menu:\n\033[m')
	for i in range(len(l)):
		print(f'\033[033m{i+1}. \033[m{l[i]}')

def tira(r):
	x = open('tabela.txt', 'r') #Abre para leitura
	linhas = x.readlines()

	prod = []
	for l in linhas: #Descobre os produtos no arquivo
		prod.append(l.split())
	x.close()

	r = r.upper()
	for i in range(len(prod)):
		aux = prod[i][0].upper()
		if r == aux:
			del(prod[i]) #exclui o produto
			break
	
	x = open('tabela.txt', 'w') #apagar o arquivo
	x.close()

	x = open('tabela.txt', 'a') #escreve os produtos de novo sem o excluido
	for i in range(len(prod)):
		for j in range(3):
			if j == 2:
				x.write(prod[i][j])
				x.write('\n')
			else:
				x.write(prod[i][j])
				x.write(' ')
	x.close()

def tabela():
	x = open("tabela.txt", 'r') #Abertura do arquivo
	linhas = x.readlines()

	prod = []
	for l in linhas: #Cada linha contém 3 informações, cada uma delas de um tipo diferente
		y = l.split()
		for i in range(3): #Esse loop recebe as informações já separadas e as add na lista já convertidas
			if i == 1:
				prod.append(float(y[i]))
			elif i == 2:
				prod.append(int(y[i]))
			else:
				prod.append(y[i])
	
	#Criação da tabela
	print("-"*44)
	print('|{:<20}{:^9}{:^13}|'.format('Produto', 'Preço', 'Quantidade'))
	print('|{:^42}|'.format('-'*38))
	i = 0
	while i < len(prod):
		print(f'|{prod[i]:<20}{prod[i+1]:^9,.2f}{prod[i+2]:^13}|')
		i += 3
	print("-"*44)

	x.close()

def notaFiscal(matriz, valor):
	print()
	print("-"*44)
	print('|{:^42}|'.format('NOTA FISCAL'))
	print("-"*44)
	print('|{:<20}{:^13}{:^9}|'.format('Produto', 'Quantidade', 'Preço'))
	print('|{:^42}|'.format('-'*38))

	for i in matriz:
		print(f'|{i[0]:<20}{i[2]:^13}{float(i[1]):^9,.2f}|')
	print("-"*44)
	print('|{:<33}{:^9,.2f}|'.format('TOTAL', valor))
	print("-"*44)
	print()

def atualizaTabela(matriz):
	x = open('tabela.txt', 'w')

	for i in range(len(matriz)):
		for j in range(3):
			x.write(matriz[i][j])
			if j == 2 and i != (len(matriz)-1):
				x.write('\n')
			elif i != (len(matriz)-1):
				x.write(' ')
	x.close()

def compra():
	totComp = 0
	comp = True

	x = open('tabela.txt', 'r') #Abre para leitura
	linhas = x.readlines()

	prod = []
	for l in linhas: #Descobre os produtos no arquivo
		prod.append(l.split())
	x.close()

	preco = 0.0 #preço total da compra
	nota = [] #nota fiscal da compra
	
	while comp == True:
		x = []
		x = input('Digite o produto q você deseja comprar e a quantidade: ').upper().split()

		if len(x) != 2:
			print('A informação passada não é válida, tente novamente.')
			continue
		elif x[0].isdigit() == True or x[1].isdigit() == False:
			print('A informação passada não é válida, tente novamente.')
			continue
		else:
			i = 0
			for i in range(len(prod)): #Verifica se existe o produto no estoque
				if x[0] != prod[i][0].upper() and i+1 == len(prod):
					i = len(prod)
					break
				elif x[0] == prod[i][0].upper():
					break
			print(f'i = {i}')
			if i != len(prod): #Encontrou o produto na lista
				for i in range(len(prod)):
					if x[0] == prod[i][0].upper():
						z = int(prod[i][2])
						w = z - int(x[1])
						fiscal = [x[0], prod[i][1]]
						if w <= 0: #Deleta se w <= 0
							if w < 0:
								w = z + (x[1] - z)
								preco += float(prod[i][1])*w #Add ao valor total
								fiscal.append(str(w))
							else:
								preco += float(prod[i][1])*int(x[1]) #Add ao valor total
								prod[i][2] = str(w)
								fiscal.append(x[1])				
							del(prod[i])
						else:
							preco += float(prod[i][1])*int(x[1]) #Add ao valor total
							prod[i][2] = str(w)
							fiscal.append(x[1])
				nota.append(fiscal[:]) #add o produto a nota fiscal que será gerada
			else:
				print(f'Não temos "{x[0]}" no estoque')

			atualizaTabela(prod)
			resp = input('Deseja continuar comprando?(S/N) ').upper()
			if resp[0] == 'S':
				comp = True
			else:
				comp = False
	notaFiscal(nota, preco)

#def ganhos():

def addi():
	x = open('tabela.txt', 'r') #Abrir para escrever no final
	print('\033[033m\nDigite o produto que você quer adicionar, seu preço com 2 casas decimais e sua quantidade em estoque:')
	print("Caso o nome do produto tenha mais de uma palavra, substitua os espaços por '-'\n")
	novo = input('Digite o produto: \033[m')
	novo = novo + "\n"
	y = novo.split()
	if len(y) != 3: #verifica se foram informadas as 3 informações necessárias
		print('\033[031m\nVocê digitou algo errado, não é possível adicionar essas informações\033[m')
		return
	elif y[0].isdigit == True or y[1].isdigit == False or y[2].isdigit == False: #verifica se as informações estão corretas
		print('\033[031m\nVocê digitou algo errado, não é possível adicionar essas informações\033[m')
		return
	else:
		r = list()
		flag = 0
		for line in x:
			w = line.split()
			if w[0].upper() == y[0].upper():
				flag = 1
				line = line.replace(str(w[1]), str(y[1]))
				line = line.replace(str(w[2]), str(y[2]))
			r.append(line)
		if flag == 0:
			r.append(novo)
		x.close()
		x = open('tabela.txt', 'w')
		for i in r:
			x.write(i)
	x.close()

def main():
	lista = ('Tabela de Produtos', 'Cálculo da compra', 'Ganhos Diários', 'Adicionar Produtos', 'Mostrar Menu', 'Sair')
	
	menu(lista)

	v = True
	while v == True:
		n = input('\033[033m\nO que você quer fazer agora? \033[m')
		if n.isdigit(): #O usuário digitou o número
			m=int(n)
			if m >= 1 and m<=6:
				if m==1:
					tabela()
				elif m==2:
					compra()
				elif m==3:
					ganhos()
				elif m==4:
					addi()
				elif m == 5:
					menu(lista)
				else:
					exit(1)
			else:
				print('A opção digitada não é válida.')
				continue
		else: #caso o usuário escreva
			if n[0] in 'Tt':
				tabela()
			elif n[0] in 'Cc':
				compra()
			elif n[0] in 'Gg':
				ganhos()
			elif n[0] in 'Aa':
				addi()
			elif n[0] in 'Mm':
				menu(lista)
			elif n[0] in 'Ss':
				exit(1)
			else:
				print('A opção digitada não é válida.')
				continue

#tira('Margarina')

main()