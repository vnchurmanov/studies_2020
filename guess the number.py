import simplegui
import random
import math

# global variable, contains the range for the current game
num_range = 100

def new_game():
    # initialize global variables
    global secret_number
    secret_number = random.randint(0, num_range)
    global guesses
    n = math.log(num_range + 1, 2)
    guesses = math.ceil(n)
    print('New game. Range is from 0 to', num_range)
    print('Number of remaining guesses is', guesses)
    print(' ')

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000
    new_game()


def input_guess(guess):
    # main game logic goes here
    global guesses
    num = int(guess)
    print('Guess was', num)
    if guesses == 0:
        print('You run out of guesses! You lose (:')
        print('The secret number was', secret_number)
        print(' ')
        new_game()
    elif secret_number > num:
        guesses -= 1
        print('Higher!')
        print('Number of remaining guesses is', guesses)
        print(' ')
    elif secret_number < num:
        guesses -= 1
        print('Lower!')
        print('Number of remaining guesses is', guesses)
        print(' ')
    else:
        print('Correct! You win!')
        print(' ')
        new_game()


# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)
# call new_game
new_game()
