# Import random for randint
import random
# Import itertools for itertools.count, count from 0 to infinite
import itertools

print("I am thinking of a number between 1 and 20.\nTake a guess.")

# Random integer from 1 to 20
x = random.randint(1,20)

# For loops for number of guess counter
# itertools.count() method count from 0 unitl the guess is correct
# Number of trial stored in the guesstaken variable
# break out of the for loop wehn the guess is correct
for guesstaken in itertools.count():
    guess = int(input())
    
    if guess < x:
        print("Too small.")
    elif guess > x:
        print("Too large.")
    else:
        break

if guess == x:
    print("Correct within " + str(guesstaken) +" trail.")