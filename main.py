from play_game import play_game

def show_menu():
    print("\n" + "═" * 40)
    print("       SCISSORS  PAPER  ROCK")
    print("═" * 40)
    print("  [1]  Start Game")
    print("  [2]  Exit")
    print("═" * 40)

def main():
    print("\n  Welcome to Scissors Paper Rock!")

    while True:
        show_menu()
        choice = input("  Enter your choice (1-2): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            print("\n  Goodbye!\n")
            break
        else:
            print("\n  Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
