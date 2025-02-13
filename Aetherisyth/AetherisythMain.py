import tkinter
import quote

'''
The purpose of this program is to
create a graphical user interface
of the application Aetherisyth,
a reading/tracker inspired app
designed in my business class.
The app itself cosists of a reading
page where users can explore various
features related to reading and a
 game page where users can play a game
that is book related.
This main page is for the initial
start that shows up with the app's
name and a start button that will
lead them to the home page of the
application.

--------------------------------------------------------
THINGS I WANT YOU TO NOTICE

- my use of a nested loop in my openRecPage module
  to give reccomendations. (I'm really proud of
  figuring that out because I really struggle with
  nested loops so this was a big achievement.) 

--------------------------------------------------------
THINGS I ACKNOWLEDGE DO NOT/DID NOT WORK
- so when you press exit app on the home page, it
  does close the home window and then there isn't
  any page left however the application is still
  running. I purposefully hid the main application
  with the root.withdraw() because if I didn't,
  any time a message box runs on my program, the
  main window pops up and that takes away from user
  experience. I tried using .deiconify() which
  is a function that pops the window back up but it
  doesn't work.
- the book of the month game only works one time,
    after you play it once, you are unable to play
    it again. While this is not the optimal situation,
    I have listed it in my instructions that if they don't
    guess properly the door will lock. This is kind of a
    one try or fail situation. I want to clarify that
    this is my intended outcome however, I acknowledge
    that for proper user interface, I would be able to
    play the game more than once.

- I was pretty sick the entire week and had a fever
  this entire weekend so I finished up to the best of
  my abilities. 

'''

#Define the Main Function
#- This is the driver of the entire program
def main():

    #ROOT WINDOW
    root = tkinter.Tk()
    root.geometry("800x450")
    root.title("Aetherisyth")

    #BACKGROUND
    #add image file
    bgImage = tkinter.PhotoImage(file = "Aetherisyth.png")

    #Create a canvas widget
    #while this was not exclusively a lesson,
    #you did a short teaching on how to do this
    #and this is where I know how to do this.
    canvasBG = tkinter.Canvas(root, width = 800, height = 450)
    canvasBG.pack(fill = "both", expand = True)
    canvasBG.create_image(0, 0, image = bgImage, anchor = "nw")


    #BUTTONS
    #the start button will start the GUI application
    #and take users to the quote page where they can
    #see a quote and then continue to the home page
    startButton = tkinter.Button(root,
                                 text = "Click to Start",
                                 bg = "#acfbe7",
                                 font = ("Times New Roman", 12),
                                 command = lambda: [root.withdraw(), 
                                                    quote.quotePage()])
                                #lambda allows you to perform two functions
                                #in a single command
                                #https://www.geeksforgeeks.org/hide-and-
                                #unhide-the-window-in-tkinter-python/
                                #.withdraw() is used to hide the window
                                #we are using the .withdraw() here because
                                #I do not want this window showing and
                                #stacking on top of the other top level
                                #windows. I will use .withdraw() multiple
                                #times in my program so I am only
                                #documenting it here. 
    
    #place the start button on the root window 
    startButton.place(x = 350, y = 350)

    #the quit button will destroy the root window
    #and users can exit out of the application through
    #this button
    quitButton = tkinter.Button(root,
                                 text = "Quit",
                                 bg = "#acfbe7",
                                 font = ("Times New Roman", 12),
                                 command = root.destroy)
    
    #place the quit button on the root window 
    quitButton.place(x = 450, y = 350) 
    

    #MAINLOOP
    tkinter.mainloop()

#Call the main function
main()


