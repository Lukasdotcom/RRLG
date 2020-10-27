#Used to decide which action the enemy does
def enemyAction(enemy):
    runChance = ((enemy["runChanceStart"] - enemy["health"]) * enemy["runChanceIncrease"]) #Calculates the chance of the enemy to run out of 100
    #Checks what action the enemy does
    if runChance > 0 and runChance < random.randint(1, 101):
        return"run"
    #This works by adding the attack and defend stat of th enemy and generating a number inbetween the added total and if that number is lower than the defense stat it defends otherwise it attacks
    elif random.randint(1, enemy["attack"] + enemy["defense"]) <= enemy["defense"]:
        return"defend"
    else:
        return"attack"
statTypesPlayer = ("defense", "attack", "maxHealth", "health", "level", "XP") #Will print these stats for the player in the info action
statTypesEnemy = ("defense", "attack", "health", "runChanceStart", "runChanceIncrease") #Will print these stats for the enemy
print("You have been attacked by a", enemy["name"]) #Tells the player who they are attacked by
#Prints the players name and the stats of the player
print(player["name"] + "'s stats")
for x in statTypesPlayer:
    print(x, ":", player[x])
print()
#does the same thing but for the enemy
print(enemy["name"] + "'s stats")
for x in statTypesEnemy:
    print(x, ":", enemy[x])
while player["health"] > 0:
    action = input("What do you want to do? Press r to run, a to attack, i for info, and d to defend: ")#used to check what action the player wants to do
    print()
    if action == "r": #If the player runs away the action is done
        print("You have ran away.")
        break
    elif action == "i": #prints all stats of the player and enemy
        #Prints the players name and the stats of the player
        print(player["name"] + "'s stats")
        for x in statTypesPlayer:
            print(x, ":", player[x])
        print()
        #does the same thing but for the enemy
        print(enemy["name"] + "'s stats")
        for x in statTypesEnemy:
            print(x, ":", enemy[x])
        continue
    enemyAct = enemyAction(enemy) #Figures out the enemy action
    if enemyAct == "run": #If the enemy runs away this does that action
        print("The", enemy["name"], "has ran away.")
        break
    elif enemyAct == "defend":
        if action == "a": #If the enemy defends and the player attacks
            damage = player["attack"] - enemy["defense"] #calculates the damage the player does
            if damage > 0: #Checks if the attack actually does damage
                enemy["health"] -= damage
                print("You succesfully damaged the", enemy["name"], "by", damage, "damage, and now the", enemy["name"], "has", enemy["health"], "HP left.")
            else:
                print("your attack was unsuccessful")
        else: #If both players defended
            print("You both blocked the attack")
    elif enemyAct == "attack":
        if action == "a":#If both players attack
            enemy["health"] -= player["attack"]
            print("You succesfully damaged the", enemy["name"], "by", player["attack"], "damage, and now the", enemy["name"], "has", enemy["health"], "HP left.")
            player["health"] -= enemy["attack"]
            print("The", enemy["name"], "succesfully atacked you with", enemy["attack"], "damage, and now you have", player["health"], "HP left.")
        else: #If the enemy attacks and player defends
            damage = enemy["attack"] - player["defense"]
            if damage > 0: #Checks if the attack actually does damage
                player["health"] -= damage
                print("The", enemy["name"], "succesfully atacked you with", damage, "damage, and now you have", player["health"], "HP left.")
            else:
                print("The", enemy["name"], "attack was unsuccessful")
    if enemy["health"] <= 0: #Checks if the enemy is dead
        print("The", enemy["name"], "has died.")#Informs player
        #Calculates XP collected and adds it to the total and tells the player
        xpGained = round(random.random() * player["level"] * 5)
        player["XP"] += xpGained
        print("You gained", xpGained, "XP")
        #Checks if the player advances to the next level and then informs the player and calculates the amount the different stats increase
        if player["XP"] >= 5 * player["level"]:
            print("You leveled up from", player["level"], "to", player["level"] + 1)
            player["XP"] -= player["level"] * 5
            player["level"] += 1
            print()
            print("New Stats for level", player["level"])
            for x in levelIncreaseMax: #This prints each stat and increases each stat by the desired amount
                 increase = random.randint(1, levelIncreaseMax[x])
                 print(x + " : " + str(player[x]) + " +" + str(increase))
                 player[x] += increase
            increase = player["maxHealth"] - player["health"]
            print("health : " + str(player["health"] + " +" + str(increase)))
            player["health"] = player["maxHealth"]
        else:#If the player does not advance to the next level they are told how much more they need to advance
            print("You need", ((player["level"] * 5) - player["XP"]), "more XP to level up.")
            
        break