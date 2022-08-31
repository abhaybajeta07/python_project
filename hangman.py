import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 6

    while len(word_letter) > 0 and lives > 0:
        print("you have", lives, "left and you have used these letters", ' '.join(used_letter))
        word_list = [letter if letter in used_letter else '_' for letter in word]
        print('current word:',' '.join(word_list))
        user_letter = input("Guess your letter").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives -1
                print(f"you have guessed it wrong ")

        elif user_letter in used_letter:
            print("you have already used this letter....try different letter")
        else:
            print("invalid character..please try again")

    if lives == 0:
        print("you died the word was", word)
    else:
        print("you guessed the word right!!!")


hangman()




