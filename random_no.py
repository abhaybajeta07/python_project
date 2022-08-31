 #new keywords used 1.random

import random


#def guess(x):
    #ran_no = random.randint(1, x)
    #guess = 0
    #while guess != ran_no:
     #   guess = int(input(f"Guess the number between 1 and {x}"))
      #  if guess > ran_no:
       #     print("nopes, too high")
        #elif guess < ran_no:
         #   print("nopes!, too low")
    #hprint(f"whohoo!!! you guessed thrr {ran_no} right!!")

#guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ' '
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high bcz low = high
        feedback = input(f"is {guess}too high (h), too low (l), or correct")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"yipee you guesses your number {guess}, correctly")

computer_guess(10)



