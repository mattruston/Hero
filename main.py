from sys import argv
from utils import *
from gameController import GameController

speedRunMode = False

def main():
    clear() # clear the terminal to a fresh state
    write("You awaken next to your fire. The flames dance in the encroaching darkness. You pick up your sword.")
    gameController = GameController()
    gameController.playGame()

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

if __name__ == "__main__":
    args = getopts(argv)
    if ("-sp" in args):
        speedRunMode = True
    main()