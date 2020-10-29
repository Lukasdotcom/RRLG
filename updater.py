files = ["battle.py", "CONTRIBUTING.md", "HELP.MD", "LICENSE", "README.md", "shop.py", "start.py", "updateChecker.py", "autosave.json"] #list of all the files that exist in this program
os.remove("updateChecker.py")#Removes the old update checker
print("Conerting saves...")
#This will convert the save
if save[1] != False: #looks if a save file even exists
    try:
        #will create the save file if possible
        player = save[1]
        with open("autoSave.json", "w") as file: 
            json.dump(player, file)
    except:#If save file creation fails will tell user
        print("Your save file was corrupted during the update process")
print("Preparing game...")
for x in files: #moves all the files out into the correct location
    os.rename((currentDirectory + "/" + update["folder"] + "/" + x), (currentDirectory + "/" + x))
os.remove(update["folder"]) #removes the old folder
print("Finished starting program.")
exec(open("start.py").read())#starts the game
