x = int(input("Digite um lado do triangulo: "))
y = int(input("Digite um lado do triangulo: "))
z = int(input("Digite um lado do triangulo: "))

if x != 0 and y != 0 and z != 0:
    if x**2 == (y**2 + z**2):
        print(f"O triangulo com os lados {x}, {y}, {z} é um triangulo reto! ")
    if x**2 > (y**2 + z**2):
        print(f"O triangulo com os lados {x}, {y}, {z} é um triangulo obtuso! ")
    if x ** 2 < (y ** 2 + z ** 2):
        print(f"O triangulo com os lados {x}, {y}, {z} é um triangulo agudo! ")
else:
    print("Os valores informados não formam um triangulo! ")