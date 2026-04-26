def decide_winner(player, computer):
    if player == computer:
        return "Draw"

    beats = {
        "rock":     "scissors",
        "scissors": "paper",
        "paper":    "rock"
    }

    if beats[player] == computer:
        return "Player"
    else:
        return "Computer"
