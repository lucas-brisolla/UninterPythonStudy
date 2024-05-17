print("Bem vindo a Livraria do Lucas Brisolla")  # Mensagem boas vindas
lista_livro = []  # Lista dos livros
id_global = 0
livro = {}


def cadastrar_livro(id):  # Função de cadastrar o livro com id nome autor e editora
    global livro
    print("-" * 50, "\n", "-" * 16, "MENU CADASTRAR LIVRO", "-" * 17, "\n")
    nome = input("Por favor entre com o nome do livro: ")  # Variáveis a respeito a dados do livro
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")
    livro = {'ID': id, 'Nome': nome, 'Autor': autor, 'Editora': editora}  # Dicionario contendo os dados do livro
    lista_livro.append(livro)  # Adiciona o dicionario livro na lista de livros
    print()


def consultar_livro():  # Função de consultar um determinado livro
    while True:
        global livro # Chamando o dicionario global livro
        print("-" * 50, "\n", "-" * 16, "MENU CONSULTAR LIVRO", "-" * 17, "\n") # Titulo do menu estilizado
        try: # Filtragem de numeros inteiros
            op = int(input(
                "Escolha a opção desejada:\n1 - Consultar Todos os livros\n2 - Consultar livro por id\n3 - Consultar livro(s) por autor\n4 - retornar\n")) # Variável que armazena o numero que será utilizado para a comparação e escolha da função
        except ValueError:
            print("Valor não inteiro, tente novamente.")
            continue
        if op == 1: # Escolha dos tipos de consulta.
            for livro in lista_livro: # Para cada "dicionario" livro dentro da lista de livros
                print() # Separar cada livro por uma linha
                for chave, valor in livro.items(): # Para cada chave e valor dentro os itens do dicionario livro
                    print(f"{chave}: {valor}") # Mostrar na tela a chave e o valor
        elif op == 2:
            try:
                id = int(input("Digite o id do livro: "))
            except ValueError:
                print("Valor não inteiro, tente novamente.")
                continue
            for livro in lista_livro:
                if livro['ID'] == id: # Se a chave 'ID' do dicionario livro for igual ao valor da variavel id
                    print()
                    for chave, valor in livro.items():
                        print(f"{chave}: {valor}")
        elif op == 3:
            autor = input("Digite o nome do autor do(s) livro(s):  ") # Se a chave 'Autor' do dicionario livro for igual ao valor da variavel autor
            for livro in lista_livro:
                if livro['Autor'] == autor:
                    print()
                    for chave, valor in livro.items():
                        print(f"{chave}: {valor}")
        elif op == 4: # Opção de sair
            break
        else: # Se nenhum valor corresponder, apresenta uma mensagem de erro
            print("Opção invaĺida!\n")
            continue


def remover_livro(): # Função que remove um item livro que possua um determinado id da lista lista_livros
    print("-" * 50, "\n", "-" * 16, "REMOVER LIVRO", "-" * 17, "\n")
    try:
        id = int(input("Digite o id do livro a ser removido:")) # Id do livro que sera removido
    except ValueError:
        print("Valor inválido")
    for livro in lista_livro:
        if livro['ID'] == id:
            lista_livro.remove(livro) # Remove o livro
        print("Livro removido com sucesso!") # Confirmação que o livro foi removido


while True: # Programa principal loop do menu até que seja selecionada a opção 4 sair
    try:
        print("-" * 50, "\n", "-" * 16, "MENU PRINCIPAL", "-" * 17, "\n")
        op_menup = int(input(
            "Escolha a opção desejada:\n1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4 - Sair\n"))
    except ValueError:
        print("Valor não inteiro")
        continue
    if op_menup == 1:
        cadastrar_livro(int(input("ID: ")))
    elif op_menup == 2:
        consultar_livro()
    elif op_menup == 3:
        remover_livro()
    elif op_menup == 4:
        break
    else:
        print("Opção inválida, tente novamente.")
        continue
