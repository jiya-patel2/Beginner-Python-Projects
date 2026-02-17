import art as a
import random
import data as d

def format_data(anime):
    anime_name = anime["Name"]
    anime_eps = anime["Episodes"]
    anime_creator = anime["Creator"]
    print(f"Name : {anime_name}\nEpisodes : {anime_eps}\nCreator : {anime_creator}")

def check(rate_a,rate_b):
    if rate_a > rate_b:
        right_option = "A"
    else: 
        right_option = "B"
    return right_option

anime_b = random.choice(d.anime_list)
def playGame(anime_b):
    currScore = 0
    print(a.logo)
    play = True
    while play:
        anime_a = anime_b
        anime_b = random.choice(d.anime_list)
        while (anime_a == anime_b):
            anime_b = random.choice(d.anime_list)
        print(f"Compare A :")
        format_data(anime_a)
        print(a.vs)
        print(f"Compare B :")
        format_data(anime_b)
        option = input("Which anime has higher rating :('A' or 'B')\n")
        rate_a = anime_a["Rating"]
        rate_b = anime_b["Rating"]
        
        if check(rate_a,rate_b) == option:
            currScore += 1
            print(f"You are correct! Current Score :{currScore}")
            if rate_a > rate_b:
                anime_b = anime_a
        else:
            print(f"Sorry that's wrong final score : {currScore}")
            break

playGame(anime_b)
