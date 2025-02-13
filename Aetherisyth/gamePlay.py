#Import Modules
import tkinter
from tkinter import *
import tkinter.messagebox
import random
import gameInstructions
import doorPage

'''
The purpose of this program is to
play the book of the month game.
Users will be playing as poppy,
a character they can move around the
screen. Scattered around the page
are 5 images of flying books aka
the clues. Each clue when clicked
will reveal a messagebox with
either information or a riddle
that users need to decipher to
get the clue. Once the users have
collected all the clues, they can
move poppy (the character) towards
the moving door which will then
open a page where they will be promted
to enter the answer to their clues. 
'''

#declare the images to be global
poppy = None
poppy_id = None #None keyword in python is null/nothing
              #this is different from zero

door = None
door_id = None

gameActive = True #flag that controls the game state
                  #a condition to stop the automatic movement
                  #of clues when poppy and a clue collide

#define the play function which will
#be the code for the playing the
#Book of the Month Game 
def play():

    #use the global image files inside the main function
    global poppy, poppy_id, door, door_id, gameActive

    #TOP LEVEL WINDOW
    playGameToplvl = tkinter.Toplevel()
    playGameToplvl.geometry("1000x600")
    playGameToplvl.title("Play Game")

    #update a widget using .configure()
    #we used this function in our lesson
    playGameToplvl.configure(background = "White")

    #CANVAS OBJECT
    #This canvas object is for the play
    #area background of where the chacracters
    #will show up. Basically this is where
    #all the clues and our player poppy will
    #be moving around and functioning.
    canvas = tkinter.Canvas(playGameToplvl, width = 950, height = 575,
                            highlightthickness = 1,
                            highlightbackground = "#5a3b3f")
    canvas.configure(background = "#5a3b3f")
    canvas.pack()

    #------------------Create the Clue Buttons-----------------------#
    #create the 5 clue buttons that will be scattered across the
    #page so that when the user clicks it, a clue will be revealed
    clueImage = tkinter.PhotoImage(file = "flyingBook.png")

    #Create the callback functions for each clue
    #when the clue button is clicked a messagebox
    #containing a clue will pop up
    def clue1():
        tkinter.messagebox.showinfo("CLUE 1", "Suzanne Collins")

    def clue2():
        tkinter.messagebox.showinfo("CLUE 2", "I’m a three-digit number,\n" +
                                    "bold and true, I start with three,\n" +
                                    "that’s your clue.\n\n" +
                                    "Next comes a number, even and fine,\n" +
                                    "Twice the square of two,\n" +
                                    "it’s in the line.\n\n" +
                                    "Finally, an even digit stands tall,\n" +
                                    "Half of eight—can you name them all?\n" +
                                    "What am I?")
    def clue3():
        tkinter.messagebox.showinfo("CLUE 3", "The antonym of utopian.")
        
    def clue4():
        tkinter.messagebox.showinfo("CLUE 4", "Unscramble the following\n" +
                                    "letter to create a word: rebelstles")
    def clue5():
        tkinter.messagebox.showinfo("CLUE 5", "I’m a number that’s even,\n" +
                                   "not odd, I’m found in February, \n" +
                                   "as many have thawed.\n\n" +
                                   "Twice fourteen, a perfect match,\n" +
                                   "Award winners often see me attached.\n\n" +
                                   "What number am I, can you catch?")
  
    #create the clue 1 button
    clue1Button = tkinter.Button(playGameToplvl, image = clueImage,
                                 command = clue1)
    
    #place on the canvas background
    clue1Button.place(x = 200, y = 120)

    #create the clue 2 button
    clue2Button = tkinter.Button(playGameToplvl, image = clueImage,
                                 command = clue2)
    clue2Button.place(x = 225, y = 400)

    #create the clue 3 button
    clue3Button = tkinter.Button(playGameToplvl, image = clueImage,
                                 command = clue3)
    clue3Button.place(x = 540, y = 120)

    #create the clue 4 button
    clue4Button = tkinter.Button(playGameToplvl, image = clueImage,
                                 command = clue4)
    clue4Button.place(x = 400, y = 25)

    #create the clue 5 button
    clue5Button = tkinter.Button(playGameToplvl, image = clueImage,
                                 command = clue5)
    clue5Button.place(x = 650, y = 400)

    #---------Menubar---------------------------#
    #the menubar is where users can manually open
    #the reading or game page and can quit the
    #page they are currently on. There will also be a
    #help option for instructions.
    
    #create a menubar and associate it with the window 
    menubar = tkinter.Menu(playGameToplvl)

    #creating the navigate menu option
    #and associating the menu to the menubar 
    navigateMenu = tkinter.Menu(menubar, tearoff = 0) #tearoff is an arguement
                                                  #that when set to 0, gets
                                                  #rid of the dotted lines
                                                  #that appear in the menu
    #creating the help menu option
    #and associating the menu to the menubar
    helpMenu = tkinter.Menu(menubar, tearoff = 0)
    
    #---------navigate menu options----------------#
    #create the menu items and add them to the navigate menu  
    navigateMenu.add_command(label = "EXIT GAME",
                             command = lambda: [playGameToplvl.destroy(),
                                                gameInstructions.instructions()
                                                ])

    #add name of Menu to menubar 
    menubar.add_cascade(label = "Navigate", menu = navigateMenu)

    #--------help menu options---------------#

    #define the callback function for the help
    #menu option- this will open a messagebox
    #that has instructions on how to navigate
    #the app.
    def openGuide():

        tkinter.messagebox.showinfo("HELP", "Welcome to the Game Page!\n" +
                                    "You are now playing the\n" +
                                    "Book of the Month Game.\n" +
                                    "Press the flying books images\n" +
                                    "to get a clue. Write the clue down\n" +
                                    "somewhere for later use.\n" +
                                    "collect all the clues and then go to\n" +
                                    "the door. There you will have to enter\n" +
                                    "the clues correctly to reveal the BotM\n" +
                                    "Remember, you only have one chance\n" +
                                    "or else the door will lock\n" +
                                    "If the door locks, exit and try again.\n"+
                                    "If you want to exit the application,\n" +
                                    "go to the naviagate menu option and\n" +
                                    "press \"EXIT GAME\".")

    #create the menu items and add them to the help menu
    helpMenu.add_command(label = "Guide", command = openGuide)

    #add name of Menu to menubar 
    menubar.add_cascade(label = "Help", menu = helpMenu)

    #configure to display the menu
    playGameToplvl.configure(menu = menubar)

    #---------------------------LOAD THE IMAGES------------------------#
    #We need to load all the images
    #that will be used in this game
    #so that we can see and play with
    #them on the canvas

    #---load the image of poppy----#
    #create image object with the image file
    poppy = tkinter.PhotoImage(file = "poppy.png")

    #assign the poppy image to the poppy_id image, so I can move it
    #the initial x and y position of the poppy image is x = 50, y = 250
    poppy_id = canvas.create_image(50, 250, anchor = NW, image = poppy)

    #---load the image of the door---#
    door = tkinter.PhotoImage(file = "door.png")
    #create the image on canvas object
    door_id = canvas.create_image(950, 50, anchor = NE,
                                    image = door)

    #-----COLLISION DETECTION-----#
    #we will have to implement the collision detection
    #manually. If poppy and the door overlap,
    #that indicates that the door module should
    #open where users can enter in their clues.
    
    #-----------------------------#
    def get_Coordinates(image_id):
        #we will use bbox which returns an approximate bounding
        #box for an item. The pixel coordiantes of minimum x,
        #minimum y, maximum x, and maximum y appear in that order.
        return canvas.bbox(image_id)
        #this returns (x1, y1, x2, y2)--the current bounding box
        #of an image--top-left(x1, y1) and
        #bottom-right (x2, y2) corners of the image's bounding box
        #on the canvas 
    
    #--define collision functions--#
    #This function checks for collisions. In the movement functions,
    #after moving their images, it checks to see if their 
    #coordinates overlap with each other--it compares
    #the bounding boxes of poppy and the clue.
    def check_Collision():
        global gameActive
        poppy_Coords = get_Coordinates(poppy_id)
        door_Coords = get_Coordinates(door_id)

        #check if the bounding boxes overlap
        #then display a messagebox if the collision is detected
        if((poppy_Coords and door_Coords) and
           (poppy_Coords[2] > door_Coords[0] and
            poppy_Coords[0] < door_Coords[2] and
            poppy_Coords[3] > door_Coords[1] and
            poppy_Coords[1] < door_Coords[3])):
            
            #Display message saying you've lost 
            doorPage.enterClues()
            
            #set the game state to inactive
            gameActive = False  


    #------POPPY MOVEMENT LOGIC-----#
    #associate the poppy image to a move function
    def move_poppy(dx, dy):
        canvas.move(poppy_id, dx, dy)

    #we need to maintain the current position of the image
    #and update it with respective distance when the arrow
    #keys are pressed  (e = event)
    def left(e):
        move_poppy(-20, 0)

    def right(e):
        move_poppy(20, 0)

    def up(e):
        move_poppy(0, -20)

    def down(e):
        move_poppy(0, 20)

    #---CLUE MOVEMENT LOGIC-----#
    #here we deal with the automatic movement of the door
    def move_door(dx, dy):
        
        #update the positions here(can be random or fixed pattern)
        canvas.move(door_id, dx, dy)
        check_Collision()
            
    def move_enemies():
        #checks to see if the game is still active 
        if gameActive:
  
            #the logic that allows the enemy to be moved randomly 
            move_door(random.randint(-8, 8),
                       random.randint(-8, 8))
            #moves every 1 second
            playGameToplvl.after(1000, move_enemies)
        

    #bind the move function to the keyboard keys
    playGameToplvl.bind("<Left>", left)
    playGameToplvl.bind("<Right>", right)
    playGameToplvl.bind("<Up>", up)
    playGameToplvl.bind("<Down>", down)

    #start the automatic movement
    move_enemies()
    
    #MAINLOOP
    playGameToplvl.mainloop()





    

