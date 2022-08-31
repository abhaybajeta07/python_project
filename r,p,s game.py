import random


def play():
    user = input("wht is your choice? 'r' for rocks, 'p' for paper, 's' scissors\n")
    computer = random.choice(['r', 'p', 's'])
    print(f"your choice {user} computers choice {computer} ")

    if user == computer:
        return 'its a tie'

    if is_win(user, computer):
        return 'you won!'

    return 'you lost'


def is_win(player , opponent):
    if (player == 'r'and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


print(play())