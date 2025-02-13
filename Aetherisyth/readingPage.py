#Import Modules
import tkinter
from tkinter import *
import tkinter.messagebox
import openRecPage
import gameInstructions 

'''
The purpose of this program is to
be the reading page for the Aetherisyth
application. The reading page will
hold various features such as the
set reading goal and a reccomendtions
page as well as a bookshelves page. 
'''
goalLabel = None

#define the reading function which will
#be the code for the reading page of the
#application.
def reading():

    global readingGoal, goalLabel 
    global enterAReview, writeThoughts, setReadingGoal
    

    #TOP LEVEL WINDOW
    readingToplvl = tkinter.Toplevel()
    readingToplvl.geometry("1000x600")
    readingToplvl.title("Reading")

    readingToplvl.configure(background = "#374d5d")

    #FRAMES

    #frame1 will hold the title image and yearly goal
    frame1 = tkinter.Frame(readingToplvl)
    frame1.pack()

    #frame2 will hold three buttons each with different functions
    frame2 = tkinter.Frame(readingToplvl)
    frame2.pack()

    #frame3 will hold the reccomendations button
    frame3 = tkinter.Frame(readingToplvl)
    frame3.pack()

    #WIDGETS

    #----------FRAME 1----------------#
    #this frame will contain the widgets
    #for the title image and the yearly goal label 

    #Title Image 
    #create image object with the image file
    readingTitleImage = tkinter.PhotoImage(file = "readingTitle.png")

    #create a label for the image 
    readingTitleLabel = tkinter.Label(frame1, image = readingTitleImage)

    #pack the label onto the frame
    readingTitleLabel.pack(side = "left")

    #Yearly Goal
    #create a label that will display
    #the reading goal
    numberRead = 0
    readingGoal = 0
    goalLabel = tkinter.Label(frame1, text = "READING GOAL\n" +
                              str(numberRead) + "/" + str(readingGoal),
                              bg = "#374d5d",
                              fg = "White",
                              height = 5,
                              width = 250, 
                              font = ("Times New Roman", 30))

    #pack the label onto frame1
    goalLabel.pack(side = "left")

    #----------FRAME 2----------------#
    #this frame will contain the widgets
    #for the 2 buttons that each have their
    #own function
    
    #Button 1 - Write Down Your Thoughts
    thoughtsButton = tkinter.Button(frame2,
                                   text = "Write Down Your Thoughts",
                                   bg = "#e2dede",
                                   height = 2,
                                   width = 50,
                                   font = ("Times New Roman", 14),
                                   command = writeThoughts)

    #pack the label onto frame2
    thoughtsButton.pack(side = "left")

    #Button 2 - Set Reading Goal
    setGoalButton = tkinter.Button(frame2,
                                   text = "Set Reading Goal",
                                   bg = "#e2dede",
                                   height = 2,
                                   width = 50,
                                   font = ("Times New Roman", 14),
                                   command = setReadingGoal)

    #pack the label onto frame2
    setGoalButton.pack(side = "right")

    #----------FRAME 3-------------------#
    #this frame will contain the widgets
    #for reccommendations button - a
    #button that will open up a toplvl window
    #and a button that will open up the
    #bookshelves page
    
    #Reccommend button
    #When users press this button
    #the reccomendations page will open
    recImage = tkinter.PhotoImage(file = "rec.png")
    recImage = recImage.zoom(2)

    recButton = tkinter.Button(frame3, image = recImage,
                               command = openRecPage.openRecPage)
    recButton.pack()

    #---------Menubar---------------------------#
    #the menubar is where users can manually open
    #the reading or game page and can quit the
    #page they are currently on. There will also be a
    #help option for instructions.
    
    #create a menubar and associate it with the window 
    menubar = tkinter.Menu(readingToplvl)

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
    navigateMenu.add_command(label = "Game",
                             command = lambda: [readingToplvl.destroy(),
                                                gameInstructions.instructions()
                                                ])

    #seperator line 
    navigateMenu.add_separator()

    #menu item 
    navigateMenu.add_command(label = "EXIT READING",
                             command = readingToplvl.destroy)

    #add name of Menu to menubar 
    menubar.add_cascade(label = "Navigate", menu = navigateMenu)

    #--------help menu options---------------#

    #define the callback function for the help
    #menu option- this will open a messagebox
    #that has instructions on how to navigate
    #the app.
    def openGuide():

        tkinter.messagebox.showinfo("HELP", "Welcome to the Reading Page!\n" +
                                    "You are now on the reading page.\n" +
                                    "Here you can explore the various\n" +
                                    "features.\n" +
                                    "The set reading goal button will\n" +
                                    "allow you to set you reading goal.\n" +
                                    "The write down your thoughts button\n" +
                                    "will take you to a page where you can\n" +
                                    "write down anything you want.\n" +
                                    "use the reccomendations button to get\n" +
                                    "a book reccomendation.\n\n"
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
    readingToplvl.configure(menu = menubar)
    
    #MAINLOOP
    readingToplvl.mainloop()

#Define the callback function for
#the thoughts Button. When this button
#is called, it will open a top level window
#where users can write down anything in a
#text widget. Afterwards they can press
#done and close the window
def writeThoughts():

    #TOP LEVEL WINDOW
    thoughtsToplvl = tkinter.Toplevel()
    thoughtsToplvl.geometry("500x500")
    thoughtsToplvl.title("Write Down Your Thoughts")

    #Create vertical scrollbar (default is vertical)
    vertScrollBar = tkinter.Scrollbar(thoughtsToplvl)

    #attach scroll bar to the window in the right side
    #and fill it vertically 
    vertScrollBar.pack(side = RIGHT, fill = Y)

    #create a text widget
    textWidget = tkinter.Text(thoughtsToplvl, width = 40, height = 20,
                              wrap = NONE, yscrollcommand = vertScrollBar.set)

    #insert some text into the textwidget
    textWidget.insert(END, "\tWrite down any\n" +
                      "\tthoughts about a book\n" +
                      "\tyou are reading. (We\n" +
                      "\tget it, sometimes books\n" +
                      "\tget you riled up and\n" +
                      "\tyou need to vent.\n" +
                      "--------------------------------------\n")

    #attach text widget to the window at the top
    textWidget.pack(side = TOP)

    vertScrollBar.config(command = textWidget.yview)

    #create the done button
    doneButton = tkinter.Button(thoughtsToplvl,
                                text = "Done",
                                fg = "White",
                                bg = "#374d5d",
                                command = thoughtsToplvl.destroy)
    doneButton.pack()

    #MAINLOOP
    thoughtsToplvl.mainloop()

#Define the callback function for
#the setGoal Button. When this button
#is called, it will open a top level window
#where users can enter the number of 
#books they wish to read. The number is then
#returned and displayed. Afterwards they can press
#done and close the window.
def setReadingGoal():
    global readingGoal
    
    #TOP LEVEL WINDOW
    goalToplvl = tkinter.Toplevel()
    goalToplvl.geometry("600x300")
    goalToplvl.title("Set a Reading Goal")

    #FRAMES
    #the top frame will be for the label
    #that gives instructions
    topFrame = tkinter.Frame(goalToplvl, relief = "raised",
                             borderwidth = 3)
    topFrame.pack()

    #the middle frame will be for the
    #entry widget where users enter the
    #number of books they have read 
    middleFrame = tkinter.Frame(goalToplvl, relief = "raised",
                                borderwidth = 3)
    middleFrame.pack()

    #the bottom frame will be for
    #the entry widget where users
    #enter the number of books they
    #wish to read 
    bottomFrame = tkinter.Frame(goalToplvl, relief = "raised",
                                borderwidth = 3)
    bottomFrame.pack()

    #WIDGETS

    #Label - gives instructions on what to do
    goalInstructLabel = tkinter.Label(topFrame,
                                      text = "Enter the Number of Books\n" +
                                      "You Have Read and Wish to Read in"
                                      "This Year\n" +
                                      "(You Can Update Anytime)",
                                      font = ("Times New Roman", 20))
    goalInstructLabel.pack()
    
    #Label - this label goes before the entry widget and
    #prompts users to enter their number
    
    #the enter read label that goes before the entry widget
    #and prompts the user to enter their number of read books 
    enterReadLabel = tkinter.Label(middleFrame,
                                   text = "Enter the number of read: ",
                                   font = ("Times New Roman", 12))
    
    #the enter goal label which goes before the entry widget and
    #prompts usrs to enter their number of books they want to read
    enterGoalLabel = tkinter.Label(bottomFrame,
                                   text = "Enter your reading goal: ",
                                   font = ("Times New Roman", 12))
    
    enterReadLabel.pack(side = "left")
    enterGoalLabel.pack(side = "left")
    
    #Entry - this is where users enter their number
    
    #Create a entry widget for the number of read books 
    readEntry = tkinter.Entry(middleFrame, width = 35)
    readEntry.pack(side = "left")

    #Create an entry widget for the number they wish to read 
    goalEntry = tkinter.Entry(bottomFrame, width = 35)
    goalEntry.pack(side = "left")

    #define the callback function for the done button.
    #This call back function will change/configure
    #the reading goal label to update to what numbers the
    #user entered 
    def done():
        global goalLabel
        goalLabel.config(text = "READING GOAL\n" +
                         str(readEntry.get()) + "/" + str(goalEntry.get()))
        
    #create the done button
    doneButton = tkinter.Button(bottomFrame, text = "Done",
                                command = lambda: [done(), goalToplvl.destroy()])
    doneButton.pack()

    #MAINLOOP
    goalToplvl.mainloop()


