#IMPORT MODULES 
import tkinter
import tkinter.messagebox
import gameInstructions
import readingPage

'''
The purpose of this program is to
make the home page of the Aetherisyth
program. This home page will only
contain a name greeting and two
buttons that can take you to the
pages of the game such as the reading
page and the game page. This is the
page where the user can navigate through
the different parts of the Aetherisyth
application and can exit the application. 
'''

#Define the homepage function which
#will contain the code for the home page
def homePage():

    #TOP LEVEL WINDOW
    homeToplvl = tkinter.Toplevel()
    homeToplvl.geometry("1000x600")
    homeToplvl.title("Home")

    #BACKGROUND
    #add image file
    bgImage = tkinter.PhotoImage(file = "homeBG.png")
    bgImage = bgImage.zoom(2)

    #Create a canvas for the background
    homeCanvas = tkinter.Canvas(homeToplvl, width = 1000, height = 600)
    homeCanvas.pack(fill = "both", expand = True)
    homeCanvas.create_image(0, 0, image = bgImage, anchor = "nw")

    #WIDGETS

    #--------labels-------------#
    #the welcome image label will
    #show the user a simple welcome statement 
    welcomeImage = tkinter.PhotoImage(file = "welcome.png")
    welcomeLabel = tkinter.Label(homeToplvl, image = welcomeImage)
    welcomeLabel.place(x = 300, y = 50)
                                 

    #--------buttons------------#
    #the reading button will direct the user to
    #the reading page, a top level window that
    #will open up once clicked

    #create image for the button
    readingImage = tkinter.PhotoImage(file = "reading.png")
    readingImage = readingImage.zoom(2)
    
    #reading (image) button 
    readingButton = tkinter.Button(homeToplvl, image = readingImage,
                                   command = readingPage.reading)
    #place on the background canvas 
    readingButton.place(x = 150, y = 250)
    
    #the game button will direct the user to
    #the game page, a top level window that
    #will open up once clicked
    
    #create image for the button
    gameImage = tkinter.PhotoImage(file = "game.png")
    gameImage = gameImage.zoom(2)
    
    #game (image) button 
    gameButton = tkinter.Button(homeToplvl, image = gameImage,
                                command = gameInstructions.instructions)

    gameButton.place(x = 550, y = 250)

    #---------Menubar---------------------------#
    #the menubar is where users can manually open
    #the reading or game page and can quit the
    #Aetherisyth application. There will also be a
    #help option for instructions.
    
    #create a menubar and associate it with the homeToplvl window 
    menubar = tkinter.Menu(homeToplvl)

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
                             command = readingPage.reading)
                        

    #this adds a line to seperate the menu items
    navigateMenu.add_separator()

    #menu item 
    navigateMenu.add_command(label = "Game",
                         command = gameInstructions.instructions)

    #seperator line 
    navigateMenu.add_separator()

    #menu item 
    navigateMenu.add_command(label = "EXIT APP",
                             command = homeToplvl.destroy)

    #add name of Menu to menubar 
    menubar.add_cascade(label = "Navigate", menu = navigateMenu)

    #--------help menu options---------------#

    #define the callback function for the help
    #menu option- this will open a messagebox
    #that has instructions on how to navigate
    #the app.
    def openGuide():

        tkinter.messagebox.showinfo("HELP", "Welcome to Aetherisyth!\n" +
                                    "You are now on the home page.\n" +
                                    "Here you can choose between either\n" +
                                    "the reading page or the game page\n" +
                                    "press the buttons labeled \"reading\"\n" +
                                    "and \"game\" to be directed to those\n" +
                                    "pages where you can explore the\n" +
                                    "features.\n" +
                                    "You can also use the navigate option\n" +
                                    "on the menu as well.\n\n" +
                                    "If you want to exit the application,\n" +
                                    "go to the naviagate menu option and\n" +
                                    "press \"EXIT APP\".")

    #create the menu items and add them to the help menu
    helpMenu.add_command(label = "Guide", command = openGuide)

    #add name of Menu to menubar 
    menubar.add_cascade(label = "Help", menu = helpMenu)

    #configure to display the menu
    homeToplvl.configure(menu = menubar)                               

    #MAINLOOP
    homeToplvl.mainloop()




