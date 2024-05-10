km_percorrido = float(input("Informe a quantidade de kilometros percorridos pelo veiculo alugado: "))
dias = int(input("Informe a quantidade de dias em que o veiculo esteve alugado: "))
preco = (dias * 60) + (km_percorrido * 0.15)
print(f"Carro alugado por {dias} dias. \n{km_percorrido} Kilometros rodados \nValor a pagar: R${preco} ")
