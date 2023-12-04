#Names

player_1 = 0
player_2 = 0
player_3 = 0
player_4 = 0

def scoreboard():
    print("\n\n\n\nScoreboard:\n" + player_1 + ": " + str(player_1_score))
    if isinstance(player_2, str):
        print(player_2 + ": " + str(player_2_score))
    if isinstance(player_3, str):
        print(player_3 + ": " + str(player_3_score))
    if isinstance(player_4, str):
        print(player_4 + ": " + str(player_4_score))
    print("\n\n")

player_1 = input("Player 1 Name: ")
answer = input("Add another player? y/n ")
if answer.lower() == "y":
    player_2 = input("Player 2 Name: ")
    answer = input("Add another player? y/n ")
    if answer.lower() == "y":
        player_3 = input("Player 3 Name: ")
        answer = input("Add another player? y/n ")
        if answer.lower() == "y":
            player_4 = input("Player 4 Name: ")

player_1_score = 301
player_2_score = 301
player_3_score = 301
player_4_score = 301

#Player_1_Throw

game_win = False
bust = False
while game_win == False:
    scoreboard()
    if bust == True:
        print("BUST!!!")
        bust = False
    print(player_1 + ", throw now.\n")
    player_1_throw = int(input("Score: "))
    if player_1_throw > player_1_score:
        bust = True
    else:
        player_1_score -= int(player_1_throw)
    if player_1_score == 0:
        game_win = True
        winner = player_1

#Player_2_Throw

    if isinstance(player_2, str) and game_win == False:
        scoreboard()
        if bust == True:
            print("BUST!!!")
            bust = False
        print(player_2 + ", throw now.\n")
        player_2_throw = int(input("Score: "))
        if player_2_throw > player_2_score:
            bust = True
        else:
            player_2_score -= int(player_2_throw)
        if player_2_score == 0:
            game_win = True
            winner = player_2

    #Player_3_Throw

    if isinstance(player_3, str):
        scoreboard()
        if bust == True:
            print("BUST!!!")
            bust = False
        print(player_3 + ", throw now.\n")
        player_3_throw = int(input("Score: "))
        if player_3_throw > player_3_score:
            bust = True
        else:
            player_3_score -= int(player_3_throw)
        if player_3_score == 0:
            game_win = True
            winner = player_3

    #Player_4_Throw

        if isinstance(player_4, str):
            scoreboard()
            if bust == True:
                print("BUST!!!")
                bust = False
            print(player_4 + ", throw now.\n")
            player_4_throw = int(input("Score: "))
            if player_4_throw > player_4_score:
                bust = True
            else:
                player_4_score -= int(player_4_throw)
            if player_4_score == 0:
                game_win = True
                winner = player_4
#Finale

scoreboard()
print(winner.upper() + " WINS!")