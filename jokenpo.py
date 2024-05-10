from random import randint

print('-' * 10, "Jokenpô Game", "-" * 10, "\n Choose your hand:\n[1] Stone\n[2] Paper\n[3] Scissor\n[0] Exit\n")
result_player = []
player_scoreboard = 0
result_pc = []
pc_scoreboard = 0
options = ("Stone", "Paper", "Scissor")

while True:
    print(f"You {player_scoreboard} vs Computer {pc_scoreboard}")
    op = int(input(":"))
    pc_op = randint(1, 3)
    if op == 0:
        print("Thanks for playing, bye! ")
        break

    elif op < 0 or op > 3:
        print("Invalid option")
        continue

    player_op = options[op - 1]
    pc_op = options[pc_op - 1]

    if pc_op == player_op:
        print("It's a Draw! ")
        result_pc.append("D")
        result_player.append("D")
        pc_scoreboard += 1
        player_scoreboard += 1
    elif (player_op == options[0] and pc_op == options[1]) or (player_op == options[2] and pc_op == options[0]) or (
            player_op == options[2] and pc_op == [1]):
        print("You win!")
        result_pc.append("L")
        result_player.append("W")
        player_scoreboard += 1
    else:
        print("Computer wins and you loose!")
        result_pc.append("W")
        result_player.append("L")
        pc_scoreboard += 1

if pc_scoreboard < player_scoreboard:
    print("You wins the jokenpô challenge congratulations!")
elif pc_scoreboard > player_scoreboard:
    print("You loose the jokenpô challenge, Try again :(")
else:
    print("Wow, It's a draw")
