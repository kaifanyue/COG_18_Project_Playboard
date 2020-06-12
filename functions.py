"""A collection of function for doing my project."""
import random
import string

def move_direction(move_dir):
    """
    Generate a move direction based on user keypress

    Parameters
    ----------
    move_dir : str
        a string that indicate directions including
        'Up', 'Down', 'Left', 'Right'

    Return
    ------
    move : list
        move dorection in vector
    """

    # get movement when receive arrows keys or aswd keys (arrow keys doesn't work on macbook sometimes)
    if move_dir == 'Up' or move_dir == 'w':
        move = [-1,0]
    elif move_dir == 'Down' or move_dir == 's':
        move = [1,0]
    elif move_dir == 'Left' or move_dir == 'a':
        move = [0,-1]
    elif move_dir == 'Right' or move_dir == 'd':
        move = [0,1]
    
    return move


def add_lists(list1,list2):
    """
    Add two input lists element by element

    Parameters
    ----------
    list1 : list
        a list of integers
    list2 : list
        a list of integers of the same size

    Return
    ------
    output : list
        The sume of the two lists
    """

    output = []

    for a,b in zip(list1,list2):
        output.append(a+b)
    
    return output


def check_bounds(position,size):
    """
    Check if the position if in the range of the size

    Parameters
    ----------
    position : list
        a two integer list
    size : int

    Return
    ------
    A boolean that indicates if the position is in the range of size
    """

    # check elements in position are not larger than size and not negative
    for n in position:
        if (n < 0)|(n>=size): 
            return False
    
    return True 


def multi_two(list):
    """
    Multiply each element in the list by two

    Parameter
    ---------
    list : ;ist
        a list of integers

    Return
    ------
    output: list
        the result of multiplyling each element in the list by two
    """

    output = []

    for n in list:
        output.append(2*n)
    
    return output


def random_coordinate(number,grid_size):
    """
    Generate a radom list of coordinates
    
    Parameters
    ----------
    number : int
        number of coordinates to generate
    grid_size : int
        the size of the playboard

    Returns
    -------
    coordinates : list
        randomly generated coordinates
    """
    coordinates = []
    # generate two numbers that are in the range of the playboard
    while len(coordinates) < number:
        num1 = random.choice(range(0,grid_size))
        num2 = random.choice(range(0,grid_size))
        # check if the coordinate already exists
        if [num1,num2] not in coordinates:
            coordinates.append([num1,num2])
    
    return coordinates


def next_move(bot):
    """
    When called, execute next step depending on what location the bot is at.

    Parameters
    ----------
    bot : Bot() type object
    """

    # check if the bot is at double step location
    # and change the boolean that controls whether should switch to double step
    if bot.position in bot.double_pos:
        bot.move_2 = not bot.move_2

    # check if the bot is at teleport position
    # and change the boolean that controls whether should perform teleport
    if bot.position in bot.tele_pos:
        bot.move_tele = not bot.move_tele
    
    # execute the move by calling corresponding method of the bot
    if bot.move_tele:
        bot.teleport()
    elif bot.move_2:
        bot.double_move()
    else:
        bot.move()


