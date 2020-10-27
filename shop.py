while True:
    choice = input("We have health potions for sale right now, press b to buy one for 10 coins, q to exit the shop, and i for info: ") #Figures out what action is wanted
    if choice == "i": #Prints info on all the different items
        print("The health potion heals you by 10 health for 10 coins.")
    elif choice == "q": #Exits the shop
        break
    elif choice == "b": #Runs the health potion buying
        while True:
            try: #Exits this if number given is not a number
                howMany = int(input("How many potions do you want to buy: ")) #Asks for the number of potions the player wants
            except: 
                print("Invalid Answer")
                continue
            if howMany < 0: #Checks that the number is positive
                print("Invalid Answer")
                continue
            if player["gold"] < howMany * 10: #Checks if the player can afford that amount of potions
                print("You can not afford this much")
                continue
            #Substracts gold from player neeeded to purchase that amount of potions and then heals the player that amount
            player["gold"] -= howMany * 10
            print("You bough", howMany, "potions.")
            player["health"] += howMany * 10
            if player["health"] > player["maxHealth"]: #Makes sure the player does not exceed the maximum amount of health
                player["health"] = player["maxHealth"]
            break
