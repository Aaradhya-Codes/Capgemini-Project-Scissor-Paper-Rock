from player_choice   import player_choice
from computer_choice import computer_choice
from decide_winner   import decide_winner
from show_result     import show_result
from show_score      import show_score

def play_game():
    player_score   = 0
    computer_score = 0
    draws          = 0

    while True:
        p = player_choice()
        c = computer_choice()
        winner = decide_winner(p, c)

        show_result(p, c, winner)

        if winner == "Player":
            player_score += 1
        elif winner == "Computer":
            computer_score += 1
        else:
            draws += 1

        show_score(player_score, computer_score, draws)

        again = input("\n  Play again? (y / n) : ").lower().strip()
        if again != "y":
            print("\n  Thanks for playing! See you next time.\n")
            break
