import random
import functions as f
import art 
import os

while True:
    choice = input("Do you want to play BlackJack('y' or 'n')\n")
    if choice == 'n':
        break
    
    os.system("cls")
    print(art.logo)
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    playerList = []
    dealerList = []
    # initial list
    for i in range(0,2):
        f.dealCards(playerList,cards)
        f.dealCards(dealerList,cards)

    # Calculating score
    playerScore =f.currentScore(playerList)
    dealerScore = f.currentScore(dealerList)
    print(f"Your cards are :{playerList} , Your Score is : {playerScore}")
    print(f"Dealer's first card is : {dealerList[0]}")
        
        # Condition to check Player's choice about getting a new card
    while playerScore < 21:
        selection = input("Do you want to get another card :\nType 'y' or 'n':\n")
        if selection == 'n':
            break
        f.dealCards(playerList, cards)
        print(f"your cards are :{playerList},your score is :{f.currentScore(playerList)}")
    playerScore = f.currentScore(playerList)

    # if player not bust then dealer turn
    if playerScore > 21:
        print("You are bust 💥")
        continue
    
    f.checkScore(dealerList, cards)
        
    # storing final scores
    dealerFinalScore = f.currentScore(dealerList)
    playerFinalScore = f.currentScore(playerList)
        
    print(f"Your cards are :{playerList} , Your Final Score is : {playerFinalScore}")
    print(f"Dealer's cards are : {dealerList} , dealer's Final Score is : {dealerFinalScore}")

    f.compare(dealerFinalScore,playerFinalScore)
