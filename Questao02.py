precos = {'CPP': 9.00, 'CPM': 14.00, 'CPG': 18.00, 'ACP': 11.00, 'ACM': 16.00, 'ACG': 20.00}
compra_total = 0
print("Bem-vindo a Loja de Gelados do Lucas Brisolla")
print("-" * 17, "Cardápio", "-" * 17)
print("-" * 44)
print("---| Tamanho | Cupuaçu (CP) | Açaí (AC) |---")
print(f"---|   P     |    R${precos['CPP']}     | R${precos['ACP']}    |---")
print(f"---|   M     |    R${precos['CPM']}    | R${precos['ACM']}    |---")
print(f"---|   G     |    R${precos['CPG']}    | R${precos['ACG']}    |---")
print("-" * 44)

while True:
    sabor = input("Entre com o sabor desejado (CP/AC): ")
    sabor = sabor.lower()
    if sabor != "ac" and sabor !="cp":
        print("Sabor inválido. Tente novamente\n")
        continue
    tamanho = input("Entre com o tamanho desejado: (P/M/G): ")
    tamanho = tamanho.lower()
    if tamanho != "p" and tamanho != "m" and tamanho != "g":
        print("Tamanho inválido. Tente novamente\n")
        continue
    if sabor == "cp" and tamanho == "p":
        pedido = precos['CPP']
        compra_total += pedido
        print(f"Voce pediu um Cupuaçu do tamanho P : R${pedido}\n")
        op = input("Deseja mais alguma coisa? (S/N): ")
        op = op.lower()
        if op == "s":
            continue
        elif op == "n":
            break
        else:
            print("Opção inválida. Tente novamente\n")
    elif sabor == "cp" and tamanho == "m":
        pedido = precos['CPM']
        compra_total += pedido
        print(f"Voce pediu um Cupuaçu do tamanho M : R${pedido}\n")
        op = input("Deseja mais alguma coisa? (S/N): ")
        op = op.lower()
        if op == "s":
            continue
        elif op == "n":
            break
        else:
            print("Opção inválida. Tente novamente\n")
    elif sabor == "cp" and tamanho == "g":
        pedido = precos['CPG']
        compra_total += pedido
        print(f"Voce pediu um Cupuaçu do tamanho G : R${pedido}\n")
        op = input("Deseja mais alguma coisa? (S/N): ")
        op = op.lower()
        if op == "s":
            continue
        elif op == "n":
            break
        else:
            print("Opção inválida. Tente novamente\n")
    elif sabor == "ac" and tamanho == "p":
        pedido = precos['ACP']
        compra_total += pedido
        print(f"Voce pediu um Açaí do tamanho P : R${pedido}\n")
        op = input("Deseja mais alguma coisa? (S/N): ")
        op = op.lower()
        if op == "s":
            continue
        elif op == "n":
            break
        else:
            print("Opção inválida. Tente novamente\n")
    elif sabor == "ac" and tamanho == "m":
        pedido = precos['ACM']
        compra_total += pedido
        print(f"Voce pediu um Açaí do tamanho M : R${pedido}\n")
        op = input("Deseja mais alguma coisa? (S/N): ")
        op = op.lower()
        if op == "s":
            continue
        elif op == "n":
            break
        else:
            print("Opção inválida. Tente novamente\n")
    elif sabor == "ac" and tamanho == "g":
        pedido = precos['ACG']
        compra_total += pedido
        print(f"Voce pediu um Açaí do tamanho G : R${pedido}\n")
        op = input("Deseja mais alguma coisa? (S/N): ")
        op = op.lower()
        if op == "s":
            continue
        elif op == "n":
            break
        else:
            print("Opção inválida. Tente novamente\n")
print()
print(f"Valor total a ser pago: R${compra_total}")