import os
import time
import sys

global speedRunMode
speedRunMode = False

def sleep(t):
    if (not speedRunMode):
        time.sleep(t)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def kill():
    sys.exit()

def write(string):
    for c in string:
        sleep(0.05)
        sys.stdout.write(c)
        sys.stdout.flush()

        if (c == "."):
           sleep(0.25) 

    sleep(0.5)
    print("")

def showOptions(intro, choices) -> int:
    write(intro)

    for x in range(len(choices)):
        display(str(x + 1) + ". " + choices[x])
        
    choice = input("\n> ")
    sleep(0.3)
    return choice

# Show options with a array of tuples (id, option)
# [ (1, "say 'hi'" ), ... ] 
# This does not return the option chosen by the user, but instead the id of the option chosen
def dialogueOptions(intro, choices):
    write(intro)
    while True:
        for i in range(len(choices)):
            display(str(i+1) + ". " + choices[i][1])

        choice = input("\n> ")
        sleep(0.3)
        if(choice.isdigit()):
            index = int(choice) - 1
            if (index >= 0 and index < len(choices)):
                return choices[index][0]
        
        specialCommands(choice)

def indexOfOption(id, options):
    for i in range(len(options)):
        if (options[i][0] == id):
            return i

def display(string):
    sys.stdout.write(string)
    sys.stdout.flush()
    sleep(0.25)
    print("")

def characterInfo(character):
    infoCard = f"""
    ------
    | () | {character.name}
    |(  )| HP: {character.health}  STR: {character.strength}
    ------
    Weapon: {character.weapon.name}
    Armor : {character.armor.name}
    """
    print(infoCard)

def specialCommands(inpt):
    if inpt == "quit" or inpt == "q":
        clear()
        print("The darkness engulfs your fire and the world around you fades to black.")
        kill()
    elif inpt == "help" or inpt == "h":
        display("\nHero's Diary:\n-------------\nTaking an action:\n\tYou can input a choice by submitting the correct action number\nExiting the game:\n\tYou can quit the game at anytime by typing 'quit' or 'q'\n")
    else:
        write("That is not an action.")