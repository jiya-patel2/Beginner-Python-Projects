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
    coins = rs_1 + (2 *rs_2) + (10*rs_10) + (5*rs_5) + (20*rs_20)
    return coins

def checkResources():
    for ingredient in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Can't make {coffee_type}, insufficient {ingredient}")

def serveOrder():
    checkResources()
    for key in MENU:
        coins = insertCoin()
        if coins < MENU[key]["cost"]:
            print(f"Not sufficient money\nYour refund is {coins}")
            break
        else :
            resources["money"] += MENU[key]["cost"]
            change = coins - MENU[key]["cost"]
            print(f"Here is Rs.{change} in change.")
            print(f"Here is your {coffee_type} ☕️. Enjoy!")
            for ingredient in MENU[coffee_type]["ingredients"]:
                resources[ingredient] -= MENU[coffee_type]["ingredients"][ingredient] 
            break
def report():
    # if customer asks for report
    print(f"Water : {resources["water"]}ml")
    print(f"Milk : {resources["milk"]}ml")
    print(f"Coffee : {resources["coffee"]}g : ")
    print(f"Money : Rs. {resources["money"]}")


# Keeping machine On for all the customers
machine = "on"
while machine == "on" :
    # ask coffee type
    coffee_type = input("What would you like? (espresso/latte/cappuccino):")
    if coffee_type == "off":
        machine == "off"
        break
    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "capuccino":
       serveOrder()
       print("\n")
    elif coffee_type == "report":
        report()
    else:
        print("Enter please recheck the Menu")

    

