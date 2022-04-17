# Replay function
import sys

mode = True
def replay():
    global mode
    while True:
        if mode == True:
            play = input("Restart Y/N:")
            if play == "Y":
                mode = True
                game()
            elif play == "N":
                sys.exit()
            else: 
                print("Type Y/N")
# Game
def game():
        print("Game Over.")
        replay()

while True:
    if mode == True:
        game()