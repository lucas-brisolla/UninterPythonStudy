total = 0
while True:
    menu = int(input("MENU Lanchonete:\n1 - Coxinha R$ 5,00\n2 - Pastel R$ 7,00\n3 - Café R$4,00\n4 - Suco R$ 6,00 \n5 - SAIR \n \nOPÇÃO:"))
    if menu == 1:
        qtd = int(input("Quantas coxinhas você deseja: "))
        preco = qtd * 5.00
        total += preco
        print(f"valor total de {qtd} coxinhas: R${preco} \n")
    elif menu == 2:
        qtd = int(input("Quantos pastéis você deseja: "))
        preco = qtd * 7.00
        total += preco
        print(f"valor total de {qtd} pastéis: R${preco} \n")
    elif menu == 3:
        qtd = int(input("Quantos cafés você deseja: "))
        preco = qtd * 4.00
        total += preco
        print(f"valor total de {qtd} cafés: R${preco} \n")
    elif menu == 4:
        qtd = int(input("Quantos sucos você deseja: "))
        preco = qtd * 6.00
        total += preco
        print(f"valor total de {qtd} sucos: R${preco} \n")
    elif menu == 5:
        print("Volte sempre!")
        break
    else:
        print("Opção inválida! Selecione novamente.")

print(f"Total a pagar R${total}")


