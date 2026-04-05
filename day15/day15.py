# import data
# should_continue=True
# #TODO 2 what would you like to have 
# def MENU_choice(choice):
#     print(data.MENU[choice]["ingredients"]) 



# #TODO 4 calculate the coins
# def coins_calc(quarters,dimes,nickles,pennies,choice):
#     print(f"here is ${change_rem} in change") 


#     value_qarter=0.25*quarters
#     value_dimes=0.10*dimes
#     value_nickles=0.05*nickles
#     value_pennies=0.01*pennies
#     total_sum=value_pennies+value_nickles+value_dimes+value_qarter
#     change_rem = total_sum-data.MENU[choice]["cost"]
#     cost = data.MENU[choice]["cost"]
#     if change_rem>0:
#         print(f"here is ${change_rem}in change")
#     elif change_rem==0:
#         print("no change is required to give")
#     else:
#         print("give the required money")

#     if total_sum >= cost:
#         return True
#     else:
#         return False
    
   


# while should_continue==True:
# #TODO 1 print all the materials 
#     print(data.resources)
#     choice1=input("what would you like to have").lower()
#     if choice1 not in data.MENU:
#         print("invalid choice")
#         continue
#     MENU_choice(choice1)




# if "water" in data.MENU[choice1]["ingredients"]:
#     if data.MENU[choice1]["ingredients"]["water"] > data.resources["water"]:
#         print("not enough water")
#         should_continue = False

# if "milk" in data.MENU[choice1]["ingredients"]:
#     if data.MENU[choice1]["ingredients"]["milk"] > data.resources["milk"]:
#         print("not enough milk")
#         should_continue = False

# if "coffee" in data.MENU[choice1]["ingredients"]:
#     if data.MENU[choice1]["ingredients"]["coffee"] > data.resources["coffee"]:
#         print("not enough coffee")
#         should_continue = False



# #TODO 3 calculate the resources available
# data.resources["water"]=data.resources["water"]-data.MENU[choice1]["ingredients"]["water"]
# data.resources["coffee"]=data.resources["coffee"]-data.MENU[choice1]["ingredients"]["coffee"]
# data.resources["milk"]=data.resources["milk"]-data.MENU[choice1]["ingredients"]["milk"]

  

# quarters1=int(input("how many quarters"))#25
# dimes1=int(input("how many dimes"))#10
# nickles1=int(input("how many nickles"))#5
# pennies1=int(input("how many pennies"))#1
# coins_calc(quarters1,dimes1,nickles1,pennies1,choice1)
# coins_calc(quarters1,dimes1,nickles1,pennies1,choice1)


import data
should_continue = True

# TODO 2 what would you like to have
def MENU_choice(choice):
    print(data.MENU[choice]["ingredients"])


# TODO 4 calculate the coins
def coins_calc(quarters, dimes, nickles, pennies, choice):
    print("please insert the coins:")

    value_qarter = 0.25 * quarters
    value_dimes = 0.10 * dimes
    value_nickles = 0.05 * nickles
    value_pennies = 0.01 * pennies

    total_sum = value_pennies + value_nickles + value_dimes + value_qarter
    cost = data.MENU[choice]["cost"]

    if total_sum >= cost:
        change_rem = round(total_sum - cost, 2)
        print(f"here is ${change_rem} in change")
        return True
    else:
        print("give the required money")
        return False


while should_continue == True:
    
    print(data.resources)

    choice1 = input("what would you like to have: ").lower()
    if choice1=="off":
        should_continue=False
        continue
    if choice1 not in data.MENU:
        print("invalid choice")
        continue

    MENU_choice(choice1)

    # ✅ separate flag (IMPORTANT FIX)
    enough_resources = True

    if "water" in data.MENU[choice1]["ingredients"]:
        if data.MENU[choice1]["ingredients"]["water"] > data.resources["water"]:
            print("not enough water")
            enough_resources = False

    if "milk" in data.MENU[choice1]["ingredients"]:
        if data.MENU[choice1]["ingredients"]["milk"] > data.resources["milk"]:
            print("not enough milk")
            enough_resources = False

    if "coffee" in data.MENU[choice1]["ingredients"]:
        if data.MENU[choice1]["ingredients"]["coffee"] > data.resources["coffee"]:
            print("not enough coffee")
            enough_resources = False

    if enough_resources == False:
        continue

    quarters1 = int(input("how many quarters: "))
    dimes1 = int(input("how many dimes: "))
    nickles1 = int(input("how many nickles: "))
    pennies1 = int(input("how many pennies: "))

    payment = coins_calc(quarters1, dimes1, nickles1, pennies1, choice1)

    if payment == False:
        continue

    # ✅ subtract AFTER payment
    if "water" in data.MENU[choice1]["ingredients"]:
        data.resources["water"] -= data.MENU[choice1]["ingredients"]["water"]

    if "coffee" in data.MENU[choice1]["ingredients"]:
        data.resources["coffee"] -= data.MENU[choice1]["ingredients"]["coffee"]

    if "milk" in data.MENU[choice1]["ingredients"]:
        data.resources["milk"] -= data.MENU[choice1]["ingredients"]["milk"]

    print(f"here is your {choice1} enjoy")