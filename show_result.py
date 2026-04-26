def show_result(player, computer, winner):
    print("\n" + "─" * 40)
    print(f"  You chose    :  {player.capitalize()}")
    print(f"  Computer chose:  {computer.capitalize()}")
    print("─" * 40)

    if winner == "Draw":
        print("  It's a Draw!")
    elif winner == "Player":
        print("  You win this round!")
    else:
        print("  Computer wins this round!")

    print("─" * 40)
