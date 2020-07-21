import random
import simplegui

name_to_number = 0
number_to_name = 0


def name_to_number(name):
    if name == 'rock':
        num = 0
    elif name == 'Spock':
        num = 1
    elif name == 'paper':
        num = 2
    elif name == 'lizard':
        num = 3
    elif name == 'scissors':
        num = 4
    else:
        num = 'error in name'
    return num

def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        name = 'error in number'
    return name

def rock():
    global name_to_number
    name_to_number = 0
    return 'rock'
def Spock ():
    global name_to_number
    name_to_number = 1
    return 'Spock'
def paper():
    global name_to_number
    name_to_number = 2
    return 'paper'
def lizard():
    global name_to_number
    name_to_number = 3
    return 'lizard'
def scissors():
    global name_to_number
    name_to_number = 4
    return 'scissors'

def 1 (player_choice):
    print (' ')
    print('Player chooses', player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    number_to_name(comp_number)
    print('Computer chooses', number_to_name(comp_number))
    diff = (comp_number - player_number) % 5
    if diff == 1 or diff == 2:
        message = 'Computer wins!'
    elif diff == 3 or diff == 4:
        message = 'Player wins!'
    else:
        message = 'Player and computer tie!'
    return print(message)
#def new_game():


# define draw handler
def draw(canvas):

    canvas.draw_text(rock, [130, 30], 30, "Green")
    canvas.draw_text(Spock, [150, 60], 30, "Green")
    canvas.draw_text(paper, [180, 60], 30, "Green")
    canvas.draw_text(lizard, [210, 60], 30, "Green")
    canvas.draw_text(scissors, [240, 60], 30, "Green")


# create frame
f = simplegui.create_frame("Камень-ножницы-бумага", 500, 300)

# register event handlers
f.add_button("rock", rock, 200)
f.add_button("Spock", Spock, 200)
f.add_button("paper", paper, 200)
f.add_button("lizard", lizard, 200)
f.add_button("scissors", scissors, 200)
f.set_draw_handler(draw)

# start frame
f.start()
#new_game()

