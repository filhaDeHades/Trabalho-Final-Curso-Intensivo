# Python's Intensive Course Final Work

Leia esse arquivo em [português](https://github.com/filhaDeHades/Trabalho-Final-Curso-Intensivo/blob/master/README_pt-BR.md)

## Purpose:
The purpose of this work is practice the lessons learned in th Python's intensive course "Fluência em Python - Do básico ao avançado".

## Specification:
Create a "system" for a store of any kind (marketplace, video shop, book store), using files.
The initial file will be a list containing the produts, its prieces and quantity stored. The products are separated in lines.

### The system must:
1. Have a menu.
2. Read the informations and create a table of products.
3. Add produts to the file.
4. Calculate the total of a store and remove the shoped products from the storage.
5. Calculate the total of all shops made during one program execution.
6. Close the program.

## Course information:
The intensive course "FLuência em Python - Do básico ao avançado" was created by [Tamires da Hora dos Santos](https://www.linkedin.com/in/tamires-da-hora-dos-santos-851a96170/ "Perfil do Linkedin") and [Marcos Augusto do Amaral](https://www.linkedin.com/in/marcos-augusto-amaral/ "Perfil do Linkedin") for the 1st Week courses of the [AsimUFF](https://www.facebook.com/Asimuff/ "Página do Facebook") team.

## Example-code menu description:
1. **Products table:** Shows all the products in the file, its priece and quantity stored.
2. **Shop:** Receives the products and how many of them will be shoped, remove the quantity shoped from the storage and add them to the shop list.
3. **Daily earnings:** Shows the total of all shops during the program execution.
4. **Add products:** Adds a new product to the storage. Also update the priece and quantity of products already stored.
5. **Show menu:** Shows the menu one more time.
6. **Exit:** Closes the program.

## Example-code functions description:
1. **menu(l):** Receives a list containing all the menu options and write them in the terminal.
2. **tabela():** Creates a table (using formatation) in the terminal using the data of the file.
3. **notaFiscal(matriz):** Receives a list of lists containing all the shopped products and writes a shop list, adding the total of the shop.
4. **atualizaTabela(matriz):** Receives a list of lists containing the updated products em puts them in the file.
5. **compra():** Makes the shopping operations and updates the storage.
6. **ganhosDia():** Writes in the terminal the daily earnings in Reals and show the products sold.
7. **addi():** Adds products to the storage.
8. **main():** Shows the menu and call the others functions.