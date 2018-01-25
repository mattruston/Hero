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

    choice = input("> ")
    sleep(0.3)
    return choice

def display(string):
    sys.stdout.write(string)
    sys.stdout.flush()
    sleep(0.5)
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