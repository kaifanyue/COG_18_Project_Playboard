"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
#import sys
#sys.path.append('../')

# Imports
from functions import move_direction, add_lists, check_bounds, multi_two, random_coordinate, next_move
from classes import Bot, AutomaticBot, ManualBot
import tkinter as tk
import tkinter.messagebox
from tkinter import*
###
###


def play_board(bot):
	"""
	Prints out the grid on a canvas every time a move is made

	Parameters
	----------
	bot : Bot() type object
	"""
	
	# create a list of dots which size is specified by grid size 
	grid_list = [[' '+chr(183)] * bot.grid_size for ncols in range(bot.grid_size)]

    # update the coordinates of teleport portals and double step onto the grid
	for pos in bot.double_pos:
		grid_list[pos[0]][pos[1]] = chr(164)
	for pos in bot.tele_pos:
		grid_list[pos[0]][pos[1]] = chr(42)

    # update the position of the bot onto the grid
	grid_list[bot.position[0]][bot.position[1]] = bot.character 

    # arrange the grid into a 2D string
	grid_update = '\n'.join(['   '.join(n) for n in grid_list])


	play_ground.delete('all')  # clear the previous print on the canvas
    
    # put instruction message on the canvas for each mode
	if var.get() == 2:
		play_ground.create_text(300,30, fill="darkblue", font="Times 15 italic bold", text = "Press arrows keys or 'aswd' keys to move around the bot.")
	else:
		play_ground.create_text(150,30, fill="darkblue", font="Times 15 italic bold", text = 'The bot is moving automaticly.')
    # put the new grid on the canvas and specify where to put it 
	play_ground.create_text(bot.grid_size*30, bot.grid_size*30, fill="darkblue", font="Times 30 italic bold", text = grid_update)    
    
    # to resolve the issue that tkinter optimized the calculation and doesn't print out each step 
	root.update()


def keyboard_control(event):
    """
    Detect keys pressed by user. Get the disired move direction by calling move_direction.
    Update the bot's attribute moves to the desired move. Exexcute the step by calling nexe_move.
    And print out the new board calling play_board.
    Modified from: https://www.daniweb.com/programming/software-development/threads/228595/getting-an-input-from-arrow-keys

    Parameters
    ----------
    event : <Key>
    	key presses are binded to the function to read what key is pressed
    """
    # quit the playboard when you press escape key
    if event.keysym == 'Escape':
        newwin.destroy()

    # to enable you move with 'aswd' keys
    elif event.char == event.keysym:
        move = move_direction(event.keysym)  # get move direction by calling move_direction 
        Manual.moves = move  # assign move direction to the manual bot's attribute 
        next_move(Manual)  # execute the move
        play_board(Manual)  # print the new board with the new move
    
    # taking account of character and other irrelevant key presses  
    elif len(event.char) == 1:
        pass
    
    # to enable you move with arrow keys
    else:
        print( 'Special Key %r' % event.keysym )  # show what key is pressed

        move = move_direction(event.keysym)  # get move direction by calling move_direction 
        Manual.moves = move  # assign move direction to the manual bot's attribute 
        next_move(Manual)  # execute the move
        play_board(Manual)  # print the new board with the new move


def new_canvas(width,height):
	"""
	create a Toplevel window and a canvas in it

	Parameters
	----------
	width : int
	height : int
	"""
	global newwin
	global play_ground

	newwin = Toplevel(root)  # create toplevel under root
	play_ground = Canvas(newwin, width = width, height=height)  # create canvas inside Toplevel
	play_ground.pack()  # pack the canvas

def start_game():
	"""
	Binded to start button to initiate the game.
	"""
	# account for unexpected user input
	try:
		# when user choose automatic mode
		if var.get() == 1:

			root.unbind_all('<Key>')  # undo command from previous manual mode
			
			# create an instance of AutomaticBot class
			global Automatic
			Automatic = AutomaticBot(double_num = int(e2.get()), grid_size = int(e1.get()), tele_num = int(e3.get()), iteration = int(e4.get()))
			
			new_canvas(Automatic.grid_size*60,Automatic.grid_size*60)  # create playboard window that can fit the grid
			play_board(Automatic)  # print out the initial position

			# run the bot for iterations specified
			for i in range(Automatic.iter):
				next_move(Automatic)  # execute the move
				play_ground.after(500,play_board(Automatic))  # delay each step by half a second

		# when user choose manual mode
		elif var.get() ==2:

			# create an instance of ManualBot class	
			global Manual
			Manual = ManualBot(double_num = int(e2.get()),grid_size = int(e1.get()),tele_num = int(e3.get()))
			
			new_canvas(Manual.grid_size*60,Manual.grid_size*60)  # create playboard window that can fit the grid
			root.bind_all('<Key>', keyboard_control)  # bind key inputs to the key reading function
			play_board(Manual)  # print out the new position

	# show warning for string input
	except ValueError:
		messagebox.showerror(title='Error', message='Please enter integers')

	# show warning for non-positive number input
	except IndexError:
		messagebox.showerror(title='Error', message='Please enter positive numbers')


def quit_game():
	"""
	Binded to quit button to exit the game window
	"""	
	root.quit()

################# GUI interface setting #####################


root = tk.Tk()  # create tkinter instance

# create entry label
tk.Label(root, text="Gird Size (7-16):", font=("Helvetica", 15)).grid(row=0, sticky = W)
tk.Label(root, text="Number of double steps ("+chr(164)+"):", font=("Helvetica", 15)).grid(row=1, sticky = W)
tk.Label(root, text="Number of teleports ("+ chr(42)+"):", font=("Helvetica", 15)).grid(row=2, sticky = W)
tk.Label(root, text="Number of iterations :", font=("Helvetica", 15)).grid(row=3, sticky = W)

# create entry box and center the input
e1 = tk.Entry(root, justify = CENTER, font=("Helvetica", 15))
e2 = tk.Entry(root, justify = CENTER, font=("Helvetica", 15))
e3 = tk.Entry(root, justify = CENTER, font=("Helvetica", 15))
e4 = tk.Entry(root, justify = CENTER, font=("Helvetica", 15))

# create default input
e1.insert(0, 10)
e2.insert(0, 6)
e3.insert(0, 6)
e4.insert(0, 50)

# place them on the window
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

# create radiobuttons for mode selection
var = IntVar() # create an IntVar to be used to differentiate which mode is selected
# create radiobuttons and assign values to them
R1 = Radiobutton(root, text="Automatic Mode", variable=var, value=1, font=("Helvetica", 15))
R1.grid(row=4, column=0)
R2 = Radiobutton(root, text="Manual Mode", variable=var, value=2, font=("Helvetica", 15))
R2.grid(row=4, column=1)

# create start button and bind with start_play function
StartButton = Button(root, text ="Start", command = start_game, font=("Helvetica", 15))
StartButton.grid(row=5, column=1)

# create quit button and bind with quit_game function
QuitButton = Button(root, text ="Quit", command = quit_game, font=("Helvetica", 15))
QuitButton.grid(row=5, column=0)

# Display GUI window in the middle of your screen. 
# Taken form https://yagisanatode.com/2018/02/24/how-to-center-the-main-window-on-the-screen-in-tkinter-with-python-3/#:~:text=Tkinter's%20geometry%20positions%20the%20window,and%20height%20of%20the%20window.
# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

# initial the GUI mainloop
root.mainloop()