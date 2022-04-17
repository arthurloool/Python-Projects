# Rock, Paper, Scissors
# Import random for random.randint()
# Import sys for sys.exit
import random, sys


# variables for record
wins = 0
losses = 0
ties = 0
    
# Player Input
# 2 Win or 2 Loss end game
print("ROCK, PAPER, SCISSORS\n2 Wins or 2 Loss End Game")
while wins < 2 and losses < 2:
    print('{} Wins, {} Losses, {} Ties'.format(wins,losses,ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playermove = input()
        if playermove == "q":
            print("Closing...")
            sys.exit() # Quit the program.
        if playermove == "r" or playermove == "p" or playermove == "s":
            break # Break out of the player input loop.
        print("Type r, p, s or q.")
    
    # Display player input
    if playermove == "r":
        print("Rock versus...")
    elif playermove == "p":
        print("Paper versus...")
    elif playermove == "s":
        print("Scissor versus...")
        
    # Display com output
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        com = "r"
        print("Rock")
    elif randomNumber == 2:
        com = "p"
        print("Paper")
    elif randomNumber == 3:
        com = "s"
        print("Scissor")
        
    # Display and record the win/loss/tie
    if playermove == com:
        ties += 1
        print("Draw")
    elif playermove == "r" and com == "s":
        wins += 1
        print("You win.")
    elif playermove == "s" and com == "p":
        wins += 1
        print("You win.")
    elif playermove == "p" and com == "r":
        wins += 1
        print("You win.")
    elif com == "r" and playermove == "s":
        losses += 1
        print("You loss.")
    elif com == "s" and playermove == "p":
        losses += 1
        print("You loss.")
    elif com == "p" and playermove == "r":
        losses += 1
        print("You loss.")
else:
    print("Game Over: {} Wins, {} Losses, {} Ties".format(wins,losses,ties))