def player_choice():
    valid = ["rock", "paper", "scissors"]
    while True:
        choice = input("\n  Enter your choice (rock / paper / scissors): ").strip().lower()
        if choice in valid:
            return choice
        print("  Invalid choice. Please enter rock, paper, or scissors.")
