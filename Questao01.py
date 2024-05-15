print("Bem-vindo a Loja do Lucas Brisolla")  # Mensagem de boas vindas
valor_unitario = float(input("Entre com o valor do produto: "))  # entrada de um valor float  "preço" do produto
qtd = int(
    input("Entre com a quantidade do produto: "))  # entrada de um valor inteiro "quantidde" para o calculo do desconto
valor_total = valor_unitario * qtd  # calculo do valor bruto
print(f"O valor SEM desconto: R${valor_total}")  # print do valor bruto
desconto1 = 4 / 100  # calculo da porcentagem
desconto2 = 7 / 100
desconto3 = 11 / 100

if valor_total >= 2500 and valor_total < 6000:  # compara valores entre 2500 e 5999 = 4
    desconto_total = valor_total * desconto1    # calculo do desconto
    print(f"O valor COM desconto: R${valor_total - desconto_total}")  # calculo do preço com descontto
elif valor_total >= 6000 and valor_total < 10000:  # compara valores entre 6000 e 9999
    desconto_total = valor_total * desconto2
    print(f"O valor COM desconto: R${valor_total - desconto_total}")
elif valor_total >= 10000:  # somente se o valor for maior ou igual a 10000
    desconto_total = valor_total * desconto3
    print(f"O valor COM desconto: R${valor_total - desconto_total}")
else:  # se o valor for menor do que 2500 ou seja nao atende nenhum dos outros casos
    print(f"O valor COM desconto: R${valor_total}")
