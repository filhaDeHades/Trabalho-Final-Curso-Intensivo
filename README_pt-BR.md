# Trabalho Final do Curso Intensivo de Python

Read this file in [english]()

## Objetivo:
Esse trabalho tem como objetivo colocar em prática o que foi aprendido durante o curso intensivo de python.
## Especificação:
Fazer o "sistema" de uma loja qualquer(mercado, locadora, livraria) utilizando arquivo.  
O arquivo inicial terá o produto, seu preço e sua quantidade em estoque.

### O sistema deve:
1. Ter um menu.
2. Ler as informações e criar uma tabela de produtos.
3. Adicionar produtos ao arquivo.
4. Calcular o valor das compras e retirar os produtos comprados do estoque.
5. Calcular o valor arrecadado durante uma execução inteira do programa.
6. fechar o programa.

## Detalhes do curso:
O curso intensivo "Fluência em Python - do básico ao avançado" foi idealizado por [Tamires da Hora dos Santos](https://www.linkedin.com/in/tamires-da-hora-dos-santos-851a96170/ "Perfil do Linkedin") e [Marcos Augusto do Amaral](https://www.linkedin.com/in/marcos-augusto-amaral/ "Perfil do Linkedin") como parte da Semana de Cursos da Equipe [AsimUFF](https://www.facebook.com/Asimuff/ "Página do Facebook").

O curso tem duração de 10hrs e foi criado para atender a ementa das matérias de "Programação de Computadores" e "Programação de Computadores I", ele também conta com um certificado de participação e apostila.

## Descrição do menu do código-exemplo:
1. **Tabela de produtos:** Mostra todos os produtos do arquivo, seu preço e sua quantidade em estoque.
2. **Compras:** Recebe os produtos a ser comprados e a quantidade deseja, retira a quantidade do arquivo e adiciona os produtos a nota fiscal que deve indicar os produtos, seus preços e suas quantidades.
3. **Ganhos Diários:** Mostra o total de tudo que foi comprado durante uma execução do programa.
4. **Adiciona Produtos:** Adiciona um produto, seu preço e sua quantidade em estoque para o arquivo.
5. **Mostrar Menu:** Mostra novamente o menu de ações possíveis.
6. **Sair:** Termina a execução do programa.

## Descrição das funções do código-exemplo:
1. **menu(l):** Recebe uma lista com o nome das opções de menu e as escreve de forma formatada no terminal.
2. **tabela():** Cria uma tabela apartir dos dados do arquivo.
3. **notaFiscal(matriz):** Recebe uma matriz com os produtos comprados, seus preços e a quantidade comprada e cria uma nota fiscal formatada com eles, adicionando o valor total da compra.
4. **atualizaTabela(matriz):** Recebe uma matriz com os produtos atualizados, seus preços e sua quantidade em estoque e os coloca no arquivo.
5. **compra():** Faz as operações de compra de produtos e atualização do estoque.
6. **ganhosDia():** Escreve no terminal os ganhos do dia em reais e a quantidade de produtos vendidos.
7. **addi():** Adiciona produtos ao estoque.
8. **main():** Mostra o menu e acha as outras funções.