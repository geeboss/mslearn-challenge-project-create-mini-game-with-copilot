# Create a game where the winner of the game is determined by three simple rules:
# 1. Rock beats Scissors
# 2. Scissors beats Paper
# 3. Paper beats Rock
# The game is multiplayer where the computer is the opponent, and can randomly choose one of the elements (Rock, Paper, Scissors) to play against the user.
# The game should be played in the console.
# The must choose one of the elements (Rock, Paper, Scissors) to play against the computer. and be warned if they enter an invalid move.
# At each round, the player can choose whether to play again or not.
# Display the user's score at the end of the game, that is after five rounds.
# The game must handle user inputs, putting them in lowercase and informing the user if an invalid choice was made.



import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    user = user.lower()
    computer = random.choice(['r', 'p', 's'])
    print(f'Computer chose {computer}.')

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # Return You win if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True
    return False

print(play())