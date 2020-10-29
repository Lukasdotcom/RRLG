files = ["battle.py", "CONTRIBUTING.md", "HELP.MD", "LICENSE", "README.md", "shop.py", "start.py", "updater.py", "autosave.json"] #List of all files that need to be deleted except for this file
update = input("Enter y if you would like to check for an update otherwise enter anything else: ") #Asks if the user wants to check for an update
try:#Removes the old version.json if it exists
    os.remove("version.json")
except:
    None
if update == "y":
    print("Looking for newest version...")
    #Downloads the json file from github and reads it
    wget.download("https://raw.githubusercontent.com/Lukasdotcom/RRLG/bugfix/version.json")
    file = open("version.json",)
    update = json.load(file)
    file.close
    if update["version"] != "v0.2.2": #Checks that a new version was released
        #Notifies the user that there is a new version and what it is and tells the user if this program crashes during the update process to reinstall the program
        print(update["version"] + " is out. It will be installed now.")
        print("If this program crashes please reinsall the program from github.")
        if update["type"] == "1": #Checks that the update uses the same protocol as the one used here
            print("cleaning...")
            try:#Saves the information in the save file
                file = open("autoSave.json",)
                saveFile = json.load(file)
                file.close
            except: #If there is no save file it says False instead
               saveFile = False 
            for x in files: #deletes all the old program files
                try:
                    os.remove(x)
                except:
                    None
            save = [2, saveFile] #First one is the save version used and the second one is the information
            print("Downloading...")
            wget.download(update["link"]) #Downloads the new program files
            print("Extracting...")
            #Extracts the downloaded zip file
            zip = zipfile.ZipFile(update["zip"]) 
            zip.extractall()
            zip.close()
            os.remove(update["zip"]) #deletes the zip file
            currentDirectory = os.getcwd() #Finds the currentDirectory
            os.rename((currentDirectory + "/" + update["folder"] + "/updater.py"), (currentDirectory + "/updater.py")) #Moves updater.py out of the extracted folder
            exec(open("updater.py").read())
        else:#Notifies user that the update protocol has changed
            print("This program does not support auto update anymore please open https://github.com/Lukasdotcom/RRLG/releases to get the latest version.")
    else: #Notifies user that they are on the latest version
        print("You are on the latest version")
