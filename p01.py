words = []

count = 1
while count <= 10:
    word = input(f"Escreva a {count}ª palavra: ")
    words.append(word)
    count += 1

vogal = []
for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
            vogal.append(letter)



print(words, "\n", vogal)
