import random

def play():
    user = input("what's your choice'r' rock, 'p' paper, 's' scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'you won!'
    return 'you lost'
def is_win(player, opponent):
    if (player == 'r' and opponent == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())