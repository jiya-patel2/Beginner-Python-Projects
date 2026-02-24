import art
print(art.logo)
dictionary ={}
flag =True
while flag:
    name = input("What is your name? ")
    bid = input("What is your bid ? : $")
    dictionary[name] = int(bid)
    #print(dictionary)
    x = input("Are there any other biders, Type yes or no:")
    if x == "yes":
        print("\n" * 20)
        flag = True
    else :
        flag = False

# user defined method
bid_list = []
for key in dictionary:
    bid_list.append(dictionary[key])
for i in range(0,len(bid_list)):
    if bid_list[i] > bid_list[i-1]:
        max_bid = bid_list[i]
for key in dictionary:
    if dictionary[key] == max_bid :
        print("Maximum bid is given by",key )

# In-built method
print("Maximum bid is given by",max(dictionary,key = dictionary.get))




