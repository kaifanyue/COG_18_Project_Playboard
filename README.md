# COG_18_Project_Playboard
Move around on a grid manual and automatically

The projecy is a board game that lets you mvoe a robot on a playground and activate special skills when you hit certain places. 
The project is built upon the artificial agents idea in A4. I expand the idea to enable user to control the bot, create special skills, and put it in a complete user interface.  
***Manual Control***   
User can control the robot in manual mode by pressing the arrow keys. This is realized by using tkinter and binding keys to a function that processes the key information.       
***Special Skills***   
I created two methods that let the bot have different move patterns. The first one is double step. When the bot step on a double step location, it will move two girds for a step until it hits another double step location. The second one is teleport. Portals are randomly generated on the board just like double step locations. When you step on a portal, you will be teleported to another portal.   
***GUI Integration***   
The manual mode is built upon tkinter so I natually put every thing on a user interface to make a better game experience. When you run the script. A window will automatically pop up. You can change the grid size, number of double step locations, number of portals and number of iterations if you choose automatic mode. Then you need to choose between manual and automatic mode, and press start button. If you enter non-positive number or string, an error message will show up. If everything is ok, a new window will pop up that shows the playboard. You can close the playboard and start a new game with new parameter for however many times you like.
######################################################################
Instruction
1. Run my_script.py and the game interface will show up.
2. Modify the parameters if you like.
3. Choose a mode by click a radio button.
4. Click Start and game board will pop up.
5. Move your arrow keys to control the bot if you chose manual mode.
6. Close the game board by pressing escape key or click the close window button. (Error may pop up in the terminal when you close the window, but it doesn't affet the game)
7. Repeat step 2-5 to play another round of game.
8. Click quit button to quit the game.
