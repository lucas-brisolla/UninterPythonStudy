tabela_precos = {'DIG': 1.10, 'ICO': 1.00, 'IPB': 0.40, 'FOT': 0.20}  # tabelade preços de acordo com a opção
extra = [15.00, 40.00]  # Valores dos serviços extras
desconto1 = 15 / 100  # Variáveis com o calculo da porcentagem de cada desconto
desconto2 = 20 / 100
desconto3 = 25 / 100

pedido = 0  # Variável para armazenar o valor do pedido selecionado de acordo com o input e seu correspondente valor da lista
pedido_total = 0  # Variável para calcular o valor do pedido * numero de páginas
preco_final = 0  # Pedido total depois do desconto
numero_paginas = 0
op_extra = 0  # Valor da opção extra

print("Bem vindo a copiadora do Lucas Brisolla")  # Mensagem de boas vindas com meu nome


def escolha_servico():  # Função de escolha dos serviços com o menu e estrutura condicional
    while True:  # Loop do menu
        global pedido  # Variável fora da função
        print(
            "Entre com o serviço desejado\nDIG - Digitalização\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocopia\n")
        servico = input().lower()  # Filtragem de maiusculas e minusculas
        if servico == "dig":  # Estrutura condicional se a variavel servico receber o input de determinada sigla, a variável pedido recebera o valor da determinada chave
            pedido = tabela_precos['DIG']
            break
        elif servico == "ico":
            pedido = tabela_precos['ICO']
            break
        elif servico == "ipb":
            pedido = tabela_precos['IPB']
            break
        elif servico == "fot":
            pedido = tabela_precos['FOT']
            break
        else:  # Se a variavel servico não for igual nenhuma das siglas. apresenta a mensagem de erro e retorna ao incio do while
            print("Escolha inválida, entre com o tipo do serviço novamente")
            continue


def num_paginas():  # Função para perguntar a quantidade de paginas e aplicar o desconto
    while True:  # Loop do menu
        global pedido_total  # Chamando as váriaveis que estão fora da função
        global numero_paginas
        global preco_final
        try:  # Filtragem de numeros inteiros
            numero_paginas = int(input("Entre com o número de páginas: "))
        except ValueError:  # Se for digitado qualquer valor que não seja um inteiro, apresenta uma mensagem de erro
            print("Por favor digite um numero inteiro.")
            continue
        if numero_paginas >= 20000:  # Limite de paginas
            print("Não aceitamos tantas páginas de uma vez.\n Por favor, entre com uma quantidade menor.")
            continue
        pedido_total = pedido * numero_paginas
        if 20 <= numero_paginas < 200:  # Estrutura condicional para realizar o calculo do preço com desconto
            desconto = pedido_total * desconto1  # Calculo do desconto
            preco_final = pedido_total - desconto  # Calculo do preco final
        elif 200 <= numero_paginas < 2000:
            desconto = pedido_total * desconto2
            preco_final = pedido_total - desconto
        elif 2000 <= numero_paginas < 20000:
            desconto = pedido_total * desconto3
            preco_final = pedido_total - desconto
        else:
            preco_final = pedido_total
        break


def servico_extra(): # Função da escolha do serviço extra
    while True:
        global preco_final # Variáveis fora do escopo da função
        global op_extra
        print(
            "Deseja adicionar algum serviço?\n1 - Encadernação Simples - R$ 15.00\n2 - Encadernação Capa Dura - R$ 40.00\n0 - Não desejo mais nada")
        try: # Filtro de numeros inteiros
            op = int(input()) # Entrada do numero equivalente ás opções
        except ValueError:
            print("Digite um valor inteiro. ")
        if op == 1: # Estrutura condicional para as escolhas dos serviços
            op_extra = extra[0] # Opção extra recebe o primeiro valor da lista dos serviços extras
            preco_final += op_extra # Calculo do preço + o preço do serviço extra
            break
        elif op == 2:
            op_extra = extra[1]
            preco_final += op_extra
            break
        elif op == 0:
            break
        else:
            print("Opção inválida\n")
            continue


escolha_servico() # Chamada das funções

num_paginas()

servico_extra()

print(f"Total: {preco_final} (serviço: {pedido} * páginas: {numero_paginas} + extra: {op_extra})") # Print final valor a ser pago
