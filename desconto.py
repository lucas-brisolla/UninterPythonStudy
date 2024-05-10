preco = float(input("Digite o preço do produto: "))
percentual = int(input("Digite a porcentagem de desconto (0-100%) : "))
desconto = percentual / 100
print(f"O produto que custa R${preco} , com o desconto de %{percentual} passa a custar R${preco * desconto}")
