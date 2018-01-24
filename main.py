from sys import argv
import utils
from gameController import GameController

def main():
    utils.clear() # clear the terminal to a fresh state
    utils.write("You awaken next to your fire. The flames dance in the encroaching darkness. You pick up your sword.")
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
    if ("-sp" in argv):
        utils.speedRunMode = True
    main()