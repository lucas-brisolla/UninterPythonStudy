norte = False
sul = False
leste = False
oeste = True
dano = 11
escudo = 1
if dano > 10 and escudo == 0:
    print("Você está morto!")
if norte or sul or leste or oeste == True:
    print("Você escapou! ")