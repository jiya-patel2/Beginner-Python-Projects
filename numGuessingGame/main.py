import art
import random as r
import function as f

while True:
    play = input("Do you want to play a new game ['yes' or 'no']:  ")
    if play == 'no':
        break
    print(art.logo)
    print("Welcome to Number Guessing Game")
    print("Guess a Number between 1 to 100")
    level = input("Choose a difficulty level 'easy' or 'hard' :\n")

    num = r.randint(1,100)
    # Level of the game
    if level == 'easy':
        f.check(10,num)
    elif level == 'hard' :
        f.check(5,num)
    else :
        print("Enter a valid Level")
