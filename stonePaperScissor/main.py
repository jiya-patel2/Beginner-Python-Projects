"""
Docstring for python.stone_paper_scissor_game

1 - input from user((ROck , papper , scissor ))
2- computer choice (computer will choose randomly)
3- result 

"""
import random
choice_list =["Rock", "Paper","Scissor"]
flag = 1
user_point = comp_point = 0
player = input("Enter your name : ")
point = int(input("Enter points required to win : "))

while(flag==1):
    if(user_point == point or comp_point == point):
        if(user_point == point):
            print("Victory!\nYou won!")
        else:
            print("Oops! You lost")
        flag=0
        break 
    # user's input 
    User_choice = input("Enter your move [from Rock, Paper, Scissor]: \n")
 
    # computer's input     
    comp_choice = random.choice(choice_list)

    print(f"{player}'s choice = {User_choice}\nComputer's choice = {comp_choice}")

    # to compare the choice 
    if(User_choice == comp_choice):
        print("Tie ...")

    elif(User_choice == "Rock"):
        if(comp_choice== "Paper"):
            print("Computer wins")
            comp_point += 1
        else:
            print(f"{player} wins")
            user_point += 1

    elif(User_choice == "Paper"):
        if(comp_choice== "Rock"):
            print("Computer wins")
            comp_point += 1
        else:
            print(f"{player} wins")
            user_point += 1
            
    elif(User_choice == "Scissor"):
        if(comp_choice== "Paper"):
            print(f"{player} wins")
            user_point += 1
        else:
            print("Computer wins")
            comp_point += 1
    
    else:
        print("Invalid choice")

print("Thank you for playing")