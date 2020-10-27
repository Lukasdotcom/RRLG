import random
print("""------Welcome to RRLG(Random Rougelike game) V0.1--------
If you need help for this game open HELP.MD""") #introduction text
names = ["Goblin", "Skeleton", "Zombie", "Snail"] #A list of all creature Names
#The amount every stat can go per level (max)
levelIncreaseMax = {
    "attack" : 20,
    "defense" : 10,
    "health" : 100
    }
#The deafult player stats
player = {
    "name" : "", 
    "attack" : 20,
    "defense" : 10,
    "health" : 100,
    "maxHealth" : 100,
    "level" : 1,
    "XP" : 0
    }
#Used to store the enemy stats
enemy = {
    "name" : "",
    "attack" : 0,
    "defense" : 0,
    "health" : 0,
    "runChanceStart" : 0, #How much health is left when the enemy has a chance to run away
    "runChanceIncrease" : 0 #How much that chance of running away increases with each health lost from the variable before(100 is a 100% chance)
    }
player["name"] = input("What is your name: ") #Asks the player what they want to be called
while True:
    #Picks a name and stores it in the enemy dictionary
    namePick = random.randint(0, len(names) - 1)
    enemy["name"] = names[namePick]
    #Calculates the stats of the enemy by taking the player level into account
    enemy["health"] = random.randint(player["level"] * 10, round(player["level"] * 60))
    enemy["attack"] = random.randint(player["level"] * 2, round(player["level"] * 12))
    enemy["defense"] = random.randint(player["level"], round(player["level"] * 6))
    #Calculates the run chance stats
    enemy["runChanceStart"] = random.randint(1, round(enemy["health"] * 0.7))
    enemy["runChanceIncrease"] = random.randint(30, 125) / enemy["runChanceStart"]
    exec(open("battle.py").read()) #Runs the actual battle
    #Checks if the [player is dead and ends the game if that is true
    if player["health"] <= 0:
        print("You died :(")
        break
    #asks for what the player wants to do next
    print()
    choice = input("If you want to attack again press enter otherwise press any key and then enter: ")
    if choice == "":
        continue
    else:
        break
