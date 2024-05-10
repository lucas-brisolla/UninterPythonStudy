menu = int(input("Selecione a fruta que deseja comprar: 1 - maçã , 2 - banana, 3 - laranja . "))
preco_maca = 2.30
preco_laranja = 3.60
preco_banana = 1.85
if menu == 1:
  qtd = int(input("Quantas unidades você deseja: "))
  valor_total = qtd * preco_maca
  if qtd > 1:
    print(f"{qtd} maçãs estão saindo por R${valor_total} .")
  else:
    print(f"{qtd} maçã está saindo por R${valor_total} .")
if menu == 2:
    qtd = int(input("Quantas unidades você deseja: "))
    valor_total = qtd * preco_banana
    if qtd > 1:
        print(f"{qtd} bananas estão saindo por R${valor_total} .")
    else:
        print(f"{qtd} banana está saindo por R${valor_total} .")
if menu == 3:
    qtd = int(input("Quantas unidades você deseja: "))
    valor_total = qtd * preco_laranja
    if qtd > 1:
        print(f"{qtd} laranjas estão saindo por R${valor_total} .")
    else:
        print(f"{qtd} laranja está saindo por R${valor_total} .")