import random

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

def rpsls(player_choice):
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

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


