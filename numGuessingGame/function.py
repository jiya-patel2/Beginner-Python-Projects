def check(totalAttempts,num):
        for i in range(totalAttempts,0,-1):
            print(f"You have {i} attempts to guess a number")
            guessNum = int(input("Make a guess :\n"))
            if guessNum == num :
                print(f"You got it! The answer is {num}")
            elif guessNum > num :
                print("Too High\nGuess again")
            else:
                print("Too low\nGuess again")