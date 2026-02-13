import random
"""
    :param playerCard: empty list to store
    :param cards: list from which cards are choosen
"""

def dealCards(playerCard,cards):
    """
    Docstring for initialCards
    To choose initial cards for both player and dealer 
    """
    playerCard.append(random.choice(cards))
    return playerCard
    
def currentScore(playerCard):
    """
    Docstring for currentScore
    Calculate sum of the cards 
    :param list of Cards initially chosen
    :return: Sum of cards
    :rtype: int
    """
    if sum(playerCard) == 21 and len(playerCard) == 2:
        return 21
    while 11 in playerCard and sum(playerCard) > 21:
        playerCard.remove(11)
        playerCard.append(1)
    return sum(playerCard)

def compare(dealerScore, playerScore):
    """
    Docstring for compare
    Compare scores of both
    """
    if playerScore > 21:
        print("You went over. You lose 🙂")
    elif dealerScore > 21 :
        print("Dealer went over. You win 🤩")
    elif dealerScore == 21 and playerScore == 21:
        print("Draw ✌️")
    elif playerScore == 21:
        print("You have Blackjack! 🤩")
    elif dealerScore == 21:
        print("Dealer has Blackjack! 🙂")
    elif playerScore > dealerScore:
        print("You won 🤩")
    elif dealerScore > playerScore:
        print("Oops You lost 🙂")
    else:
        print("Draw ✌️")


def checkScore(playerCards,cards):
    """
    Docstring for checkScore
    Condition to check if the dealer has sum > 17
    :param playerCards: Description
    :param cards: Description
    """
    
    while (currentScore(playerCards) < 17):
        dealCards(playerCards,cards)
    return playerCards