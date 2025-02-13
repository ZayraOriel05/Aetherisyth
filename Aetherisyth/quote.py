import tkinter
import random
import home

'''
The purpose of this program is to
create the quotes page of the Aetherisyth
application. This page is to randomly
generate a quote. This page acts as a
transition from the start page to the 
home page which is one of the features
of the Aetherisyth application.
After the user sees the quote, they can
continue to the home page. 
'''

#This function will deal with opening a new window
#that displays a randomized quote
def quotePage():

    #TOP LEVEL WINDOW 
    quoteToplvl = tkinter.Toplevel()
    quoteToplvl.geometry("800x450")
    quoteToplvl.title("Quote")

    #BACKGROUND
    #add image file
    quoteImage = tkinter.PhotoImage(file = "quotebg.png")
    
    #Create a canvas widget
    #while this was not exclusively a lesson,
    #you did a short teaching on how to do this
    #and this is where I know how to do this.
    quoteCanvasBG = tkinter.Canvas(quoteToplvl, width = 800, height = 450)
    quoteCanvasBG.pack(fill = "both", expand = True)
    quoteCanvasBG.create_image(0, 0, image = quoteImage, anchor = "nw")

    #Labels (quotes) for top level window
    #assign each quote so that we can use all
    #the quotes in a list and then randomize
    #the list 
    fantasyQuote = "\"The moment you doubt \nwhether you can fly," + \
                   "\nyou cease for ever \nto be able to do it."
    romanceQuote = "\"The heart is an arrow.\n" + \
                   "It demands aim to land true.\""
    famousQuote = "\"Libraries were full of \nideas—perhaps" + \
                  "\nthe most dangerous and \npowerful of all weapons.\""

    #make a list that holds all the quotes defined 
    quoteList = [fantasyQuote, romanceQuote, famousQuote]

    #create the label for the quotes
    #random.choice randomly chooses
    #from the list 
    quoteWindowLabel = tkinter.Label(quoteToplvl,
                                 text = random.choice(quoteList),
                                 bg = "#acfbe7",
                                 font = ("Times New Roman", 25))

    #Place on the canvas 
    quoteWindowLabel.place(x = 200, y = 100)

    #Button to next page
    continueButton = tkinter.Button(quoteToplvl,
                                    text = "Continue",
                                    bg = "#e2dede",
                                    font = ("Times New Roman", 18),
                                    command = lambda: [quoteToplvl.destroy(),
                                                       home.homePage()])
    #place the continue button on the canvas
    continueButton.place(x = 650, y = 375)
                                
    
    #MAINLOOP
    quoteToplvl.mainloop()

                        

