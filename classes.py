import random
import string
from functions import move_direction, add_lists, check_bounds, multi_two, random_coordinate, next_move

class Bot():
    """
    A class that stores the bot's movement and location. 
    And define some parameters of the playboard. (Modified from A4)
    
    Parameters
    ----------
    double_num : int, optional
        Number of points to transit to double step movement. default = 4
    grid_size : int, optional
        Board size. default = 10
    tele_num : int, optional
        NUmber of teleporting portals. default = 4.
    """

    def __init__(self, double_num = 4, grid_size = 10, tele_num = 4):

        self.character  = chr(8982)
        self.position = [3,3]
        self.moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.grid_size = grid_size
        self.move_2 = False
        self.move_tele = False
        self.double_num = double_num
        self.tele_num = tele_num
        self.last_move = None


class AutomaticBot(Bot):
    """
    A automatic bot class that inherits from Bot class. (Modified from A4 WonderBot)
    
    Parameters
    ----------
    double_num : int, optional
        Number of points to transit to double step movement. default = 4
    grid_size : int, optional
        Board size. default = 10
    tele_num : int, optional
        Number of teleporting portals. default = 4.
    iteration : int, optional
        Numner of iterations to run the bot. default = 50
    """

    def __init__(self, double_num = 4, grid_size = 10, tele_num = 4, iteration = 50):

        super().__init__(double_num, grid_size, tele_num)

        # generate a random list of double step positions
        # by calling random_coordinate function
        self.double_pos = random_coordinate(self.double_num, self.grid_size)
        # generate a random list of teleport positions calling the same function
        self.tele_pos = random_coordinate(self.tele_num, self.grid_size)
        self.iter = iteration
        # the probablity that the bot maintain its previous direction
        self.prob = 0.5
    
    def biased_choice(self):
        """
        Randomly generate a move direction that is under the preset probability of maintaing
        its original direction.
    
        Parameters
        ----------
        self.last_move : int
            class attribute that stores the last move. default = None
        self.prob : float
            class attribute that stores the probablity of maintaining last direction.
        self.moves : list
            class attribute that stores list of movement in four directions

        Return
        ------
        move : list
            contains two integers that tells the direction of movement 
        """

        move = None
        if self.last_move != None:
            if random.random() < self.prob:  # generate a random number from 0 to 1 and compare with prob
                move = self.last_move
        if move == None:  # make a random movement in case there is no last movement
            move = random.choice(self.moves)
        
        return move
    
    def move(self):
        """
        Make a step movement by updating a randomly generated movement 
        to the new position. 
    
        Parameters
        ----------
        self.grid_size : int
            class attribute that stores the size of the playboard.
        self.last_move : list
            class attribute that stores the current movement to be used by next step.
        
        Return
        ------
        self.position : list
            class attribute that stores the updated position of the bot.
        """

        has_new_pos = False
        while not has_new_pos:
            move = self.biased_choice()  # get a movement direction
            new_pos = add_lists(self.position, move)  # add to original position
            has_new_pos = check_bounds(new_pos, self.grid_size)  # check if in the bound
            self.lase_move = move
        
        self.position = new_pos  # assign new position to attribute
    
    def double_move(self):
        """
        Make a two step movement by multiply a randomly generated movement by two.
        And update to the new position. 
    
        Parameters
        ----------
        self.grid_size : int
            class attribute that stores the size of the playboard.
        self.last_move : list
            class attribute that stores the current movement to be used by next step.
        
        Return
        ------
        self.position : list
            class attribute that stores the updated position of the bot.
        """       
        has_new_pos = False
        while not has_new_pos:
            move = multi_two(self.biased_choice())
            new_pos = add_lists(self.position, move)
            has_new_pos = check_bounds(new_pos, self.grid_size)
            self.last_move = move
        
        self.position = new_pos
    
    def teleport(self):
        """
        Move to a random portal position that is not current position.
    
        Parameters
        ----------
        self.tele_pos : list
            class attribute that stores the portal positions.
        
        Return
        ------
        self.position : list
            class attribute that stores the updated position of the bot.
        """             
        has_new_pos = False
        while not has_new_pos:
            new_pos = random.choice(self.tele_pos)  # randomly choose a protal
            if new_pos != self.position:  # check if it's at the same position
                has_new_pos = True
        
        self.position = new_pos


class ManualBot(Bot):
    """
    A manual bot class that inherits from Bot class. 

    Parameters
    ----------
    double_num : int, optional
        Number of points to transit to double step movement. default = 4
    grid_size : int, optional
        Board size. default = 10
    tele_num : int, optional
        Number of teleporting portals. default = 4
    """

    def __init__(self, double_num = 4, grid_size = 10, tele_num = 4):

        super().__init__(double_num, grid_size, tele_num)

        # generate a random list of double step positions
        # by calling random_coordinate function
        self.position = [0,0]
        self.double_pos = random_coordinate(self.double_num, self.grid_size)
        # generate a random list of teleport positions calling the same function
        self.tele_pos = random_coordinate(self.tele_num, self.grid_size)
    
    def move(self):
        """
        Make a step movement by adding the user input movement to original position. 
    
        Parameters
        ----------
        self.grid_size : int
            class attribute that stores the size of the playboard.
        self.moves : list
            class attribute that stores the user input direction.
        
        Return
        ------
        self.position : list
            class attribute that stores the updated position of the bot.
        """
        new_pos = add_lists(self.position,self.moves)
        # make sure the new position is in the bound
        has_new_pos = check_bounds(new_pos,self.grid_size)
        if has_new_pos == False:
            pass
        elif has_new_pos == True:
            self.position = new_pos

    def double_move(self):
        """
        Make a two step movement by adding the user input movement to original position. 
    
        Parameters
        ----------
        self.grid_size : int
            class attribute that stores the size of the playboard.
        self.moves : list
            class attribute that stores the user input direction.
        
        Return
        ------
        self.position : list
            class attribute that stores the updated position of the bot.
        """
        move = multi_two(self.moves)
        new_pos = add_lists(self.position,move)

        has_new_pos = check_bounds(new_pos,self.grid_size)
        if has_new_pos == False:
            pass
        elif has_new_pos == True:
            self.position = new_pos
    
    def teleport(self):
        """
        Move to a random portal position that is not current position.
    
        Parameters
        ----------
        self.tele_pos : list
            class attribute that stores the portal positions.
        
        Return
        ------
        self.position : list
            class attribute that stores the updated position of the bot.
        """             
        has_new_pos = False
        while not has_new_pos:
            new_pos = random.choice(self.tele_pos)  # choose a portal randomly
            if new_pos != self.position:
                has_new_pos = True

        self.position = new_pos