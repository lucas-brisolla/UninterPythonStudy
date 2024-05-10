notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
contagem = 0
print(notas)

for nota in notas:
    if nota == 7:
        contagem += 1

notas[-1] = 4
print(contagem)
print(notas)
print(max(notas))
notas.sort()
print(notas)

total = 0
for nota in notas:
    total += nota

print(total / len(notas))
print(sum(notas) / len(notas))

print(notas.count(7))
