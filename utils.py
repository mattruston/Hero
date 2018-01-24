import os
import time
import sys
import main

def sleep(t):
    time.sleep(t)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def write(string):
    for c in string:
        if (not main.speedRunMode):
            sleep(0.05)
        sys.stdout.write(c)
        sys.stdout.flush()

        if (c == "."):
           sleep(0.25) 

    sleep(0.5)
    print("")


def showOptions(choices) -> int:
    write("What do you do?")

    for x in range(len(choices)):
        display(str(x) + ". " + choices[x])

    choice = input("> ")
    sleep(0.3)
    return choice
        # try:
        #     value = int(choice)
        #     if (value >= 0 and value < len(choices)):
        #         return value
        # except:
        #     pass

        # display("Invalid command") 


def display(string):
    sys.stdout.write(string)
    sys.stdout.flush()
    sleep(0.5)
    print("")