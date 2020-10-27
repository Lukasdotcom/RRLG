import random, json, os
def newGame():#Used for a new game
    global player
    #The deafult player stats
    player = {
        "name" : "", 
        "attack" : 20,
        "defense" : 10,
        "health" : 5,
        "maxHealth" : 100,
        "level" : 1,
        "XP" : 0,
        "gold" : 0
        }
    player["name"] = input("What is your name: ") #Asks the player what they want to be called
print("""------Welcome to RRLG(Random Rougelike game) V0.2 - Shop and Save Prerelease--------
If you need help for this game open HELP.md""") #introduction text
names = ["Goblin", "Skeleton", "Zombie", "Snail"] #A list of all creature Names
statTypesPlayer = ("defense", "attack", "maxHealth", "health", "level", "XP", "gold") #Will print these stats for the player in the info action
statTypesEnemy = ("defense", "attack", "health", "runChanceStart", "runChanceIncrease") #Will print these stats for the enemy
#The amount every stat can go per level (max)
levelIncreaseMax = {
    "attack" : 20,
    "defense" : 10,
    "health" : 100
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
try:#Checks if there is a save file and loads it if it exists
    file = open("autoSave.json",)
    player = json.load(file)
    file.close
except:#If there is no save file or the user chose to make a new game it makes a new game
    newGame()
while True:
    #autosaves the game
    with open("autoSave.json", "w") as file: 
        json.dump(player, file)
    #asks for what the player wants to do next
    print()
    choice = input("If you want to attack again press a, if you want to shop press s, if you want player stats press i, if you want to restart press r and press anything else to quit: ")
    if choice == "a":
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
            try:
                os.remove("autoSave.json")
            except:
                None
            print("You died :(")
            break
    elif choice == "s":
        exec(open("shop.py").read()) #Runs the shop file
    elif choice == "i":
        #Prints the players name and the stats of the player
        print(player["name"] + "'s stats")
        for x in statTypesPlayer:
            print(x, ":", player[x])
    elif choice == "r":
        newGame()
    else:
        break
