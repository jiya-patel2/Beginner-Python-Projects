MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 75,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 100,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 150,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0,
}

def insertCoin():
    # inserting coins
    rs_1 =  int(input("Enter number of 1 rupees coins :"))
    rs_2 =  int(input("Enter number of 2 rupees coins :"))
    rs_5 =  int(input("Enter number of 5 rupees coins :"))
    rs_10 =  int(input("Enter number of 10 rupees coins :"))
    rs_20 =  int(input("Enter number of 20 rupees coins :"))
    coins = rs_1 + (rs_2) + (rs_10) + (rs_5) + (rs_20)
    return coins

# Keeping machine On for all the customers
machine = "on"
while machine == "on" :
    # ask coffee type
    coffee_type = input("What would you like? (espresso/latte/cappuccino):")
    coins = 0
    if coffee_type == "off":
        machine == "off"
        break
    elif coffee_type == "espresso":
        insertCoin()
        if coins < MENU["espresso"]["cost"]:
            break
        else :
            resources["money"] += MENU["espresso"]["cost"]
            change = coins - MENU["espresso"]["cost"]
            resources[""]
            print(f"Here is Rs.{change} in change.")
            print("Here is your espresso ☕️. Enjoy!")
    
        print("\n")
    elif coffee_type == "latte":
        resources["money"] += MENU["latte"]["cost"]
        print("\n")
    elif coffee_type == "cappuccino":
        resources["money"] += MENU["cappuccino"]["cost"]
        print("\n")
    elif coffee_type == "report":
        # if customer asks for report
        print(f"Water : {resources["water"]}ml")
        print(f"Milk : {resources["milk"]}ml")
        print(f"Coffee : {resources["coffee"]}g : ")
        print(f"Money : Rs. {resources["money"]}")

    

