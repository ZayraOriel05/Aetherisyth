import tkinter
from tkinter import *
import tkinter.messagebox
import readingPage 
import gamePlay 

'''
The purpose of this program is to
give the users instructions on how
to play the Book of the Month game.
This is basically a landing page where
users recieve instructions for the
game and then they can start the
game. 
'''

#Define the instructions function
#this will run the code for this
#entire page
def instructions():

    #TOP LEVEL WINDOW
    gameToplvl = tkinter.Toplevel()
    gameToplvl.geometry("1000x600")
    gameToplvl.title("Book of the Month Game")

    #configure the background of the
    #top level to a colour 
    gameToplvl.configure(bg = "#5a3b3f")

    #FRAMES
    #the top frame will be for the heading label 
    topFrame = tkinter.Frame(gameToplvl)
    topFrame.pack()

    #the middle frame will be for the subheading label
    middleFrame = tkinter.Frame(gameToplvl)
    middleFrame.pack()
    
    #the bottom frame will be for the character,
    #intstructions, and start button
    bottomFrame = tkinter.Frame(gameToplvl)
    bottomFrame.pack()

    #WIDGETS

    #--------------Labels-------------#
    #the labels will be the heading of the game and the
    #subheading which can be found on the topFrame and middleFrame

    #The BotM label is the one that displays the name of the game
    #the heading for Book of the Month Game
    BotMLabel = tkinter.Label(topFrame,
                              text = "Book of the Month Game",
                              bg = "#5a3b3f",
                              fg = "White",
                              width = 450,
                              font = ("Times New Roman", 61))
    #pack the BotMLabel onto the window
    BotMLabel.pack(side = "top")

    #The subheading which is the phrase label will display a short
    #phrase that captures the essence of the game
    phraseLabel = tkinter.Label(middleFrame,
                                text = "Gather the Clues to" +
                                " Unlock the Door and Reveal the" +
                                " Book of the Month.",
                                bg = "#5a3b3f",
                                fg = "White",
                                width = 450,
                                height = 3,
                                font = ("Times New Roman", 22))
    #pack the phraseLabel onto the window
    phraseLabel.pack()

    #-------------Image------------#
    #create the image of poppy 
    poppyImage = tkinter.PhotoImage(file = "poppy.png")
    poppyLabel = tkinter.Label(bottomFrame, image = poppyImage)
    poppyLabel.pack(side = "left")

    #------------Instructions (text widget and scrollbar)-----------#
    #Create vertical scrollbar (default is vertical)
    vertScrollBar = tkinter.Scrollbar(bottomFrame)

    #attach scroll bar to the window in the right side
    #and fill it vertically 
    vertScrollBar.pack(side = RIGHT, fill = Y)
    
    #create a text widget 
    instructionsText = tkinter.Text(bottomFrame, width = 40, height = 18,
                              wrap = NONE, yscrollcommand = vertScrollBar.set)

    #insert some text into the textwidget
    instructionsText.insert(END, "\t\tINSTRUCTIONS\n\n" +
                            "You are playing as this character\n" +
                            "(Poppy)positioned on the left.\n\n" + 
                            
                            "Soon you will enter an empty room where\n" + 
                            "flying books will appear.\n\n" + 

                            "Your goal is to capture the flying\n" +
                            "objects by clicking on them to reveal a\n" +
                            "clue.\n\n" +  

                            "After you click the object,\n" +  
                            "a messagebox with information will\n" +  
                            "appear.\n\n" + 

                            "It may be a number or a word you need\n" +  
                            "to unscramble.\n\n" + 

                            "You need somewhere to write down your\n" +
                            "answers (or you can memeorize them.)\n\n" +

                            "After collecting all the flying objects\n" +
                            "and clues, you must go to the door and\n" +
                            "enter all your answers.\n\n" +

                            "The door will ask for them in a\n" +
                            "specific order and it is timed so\n" +
                            "you must answer them quickly.\n\n" +

                            "If you answer all of them correctly,\n" +
                            "the Book of the Month will be revealed.\n\n" +

                            "Otherwise the door will lock")
    
    #attach text widget to the window at the top
    instructionsText.pack(side = "left")

    vertScrollBar.config(command = instructionsText.yview)

    #-----------Start Button--------------------#
    #when the user presses the start button, they will be
    #exited from the instructions page and will be taken
    #to the game page where they will play the game
    #this essentially starts the game.
    startButton = tkinter.Button(bottomFrame,
                                 text = "START GAME",
                                 bg = "#e2dede",
                                 height = 3,
                                 width = 15,
                                 command = lambda: [gameToplvl.destroy(),
                                                    gamePlay.play()])
                                    
                                #the command for the startButton
                                #will be to open the playGame module that
                                #contains the code for actually playing
                                #the game.
    startButton.pack(side = "left")

    #---------Menubar---------------------------#
    #the menubar is where users can manually open
    #the reading or game page and can quit the
    #page they are currently on. There will also be a
    #help option for instructions.
    
    #create a menubar and associate it with the window 
    menubar = tkinter.Menu(gameToplvl)

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
    navigateMenu.add_command(label = "Reading",
                             command = lambda: [gameToplvl.destroy(),
                                                readingPage.reading()
                                                ])

    #seperator line 
    navigateMenu.add_separator()

    #menu item 
    navigateMenu.add_command(label = "EXIT GAME",
                             command = gameToplvl.destroy)

    #add name of Menu to menubar 
    menubar.add_cascade(label = "Navigate", menu = navigateMenu)

    #--------help menu options---------------#

    #define the callback function for the help
    #menu option- this will open a messagebox
    #that has instructions on how to navigate
    #the app.
    def openGuide():

        tkinter.messagebox.showinfo("HELP", "Welcome to the Game Page!\n" +
                                    "You are now on the game page.\n" +
                                    "Here you can read the instructions\n" +
                                    "on how to play the Book of the Month\n" +
                                    "game, and when you ready, press start\n" +
                                    "to begin the game.\n" +
                                    "Use the navigate option to go to a\n" +
                                    "different page.\n" +
                                    "If you want to exit the application,\n" +
                                    "go to the naviagate menu option and\n" +
                                    "press \"EXIT READING\".")

    #create the menu items and add them to the help menu
    helpMenu.add_command(label = "Guide", command = openGuide)

    #add name of Menu to menubar 
    menubar.add_cascade(label = "Help", menu = helpMenu)

    #configure to display the menu
    gameToplvl.configure(menu = menubar)

    #MAINLOOP
    gameToplvl.mainloop()



