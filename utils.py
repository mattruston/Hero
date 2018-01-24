import os
import time
import sys

global speedRunMode
speedRunMode = True

def sleep(t):
    if (not speedRunMode):
        time.sleep(t)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def write(string):
    for c in string:
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

def display(string):
    sys.stdout.write(string)
    sys.stdout.flush()
    sleep(0.5)
    print("")