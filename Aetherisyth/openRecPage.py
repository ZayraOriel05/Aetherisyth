import tkinter
import tkinter.messagebox

'''
The purpose of this proggram is to
give reccomendations based on what the
user chooses. This is apart of the
Aetherisyth application and is a
feature of the reading page.
This page will contain options to
select from and when the user chooses
from those options, it will give a
reccomendation. 
'''

#Define the callback function for the
#reccommendations button. When this button
#is called, it will open a top level window
#where users can choose from a list of
#choices and afterwards, a book reccomendation
#will be shown.
def openRecPage():

    #TOPLEVEL WINDOW
    recToplvl = tkinter.Tk()
    recToplvl.geometry("500x500")
    recToplvl.title("Recommendations")

    #---FRAMES---#
    #Instruction frame - this frame will
    #hold the instructions for this page 
    instructFrame = tkinter.Frame(recToplvl, relief = "raised",
                                  borderwidth = 2)
    instructFrame.pack()

    #ageRating Frame - this frame will hold
    #everything that is related to the age rating 
    ageRatingFrame = tkinter.Frame(recToplvl, relief = "raised",
                                  borderwidth = 2)
    ageRatingFrame.pack()

    #genre Frame - this frame will hold everything
    #that is realted to the genre 
    genreFrame = tkinter.Frame(recToplvl, relief = "raised",
                                  borderwidth = 2)
    genreFrame.pack()
    
    #button frame - this frame will hold the
    #buttons, ok and quit 
    buttonFrame = tkinter.Frame(recToplvl, relief = "raised",
                                  borderwidth = 2)
    buttonFrame.pack()

    #---------------INSTRUCT FRAME-------------#
    #create a label widget for the intstructions
    instructLabel = tkinter.Label(instructFrame, text = "Hello!\n" +
                                  " Choose One option from the following\n" +
                                  " sections to get a book recommendation.",
                                  bg = "#374d5d",
                                  fg = "White",
                                  font = ("Times New Roman", 18))
    instructLabel.pack()

    #----------HEADING LABELS-----------------#
    #create three headings for each category of
    #radiobuttons

    #age rating label 
    ageRatingLabel = tkinter.Label(ageRatingFrame,
                               text = "Choose a Age Rating",
                               bg = "#374d5d",
                               fg = "White",
                               font = ("Times New Roman", 18))
    ageRatingLabel.pack()

    #genre label 
    genreLabel = tkinter.Label(genreFrame,
                                text = "Choose a Genre",
                                bg = "#374d5d",
                                fg = "White",
                                font = ("Times New Roman", 18))
    genreLabel.pack()
                                 
    #---RADIOBUTTONS---#
    #create an IntVar object to use with the Radiobuttons
    
    #the radioVar1 will deal with the age rating
    #radiobuttons 
    radioVar1 = tkinter.IntVar(recToplvl)

    #set the IntVar object to 1
    radioVar1.set(1) #calls the radioVar object's set method to store
                    #the integer value 1 in the object
    
    #the radioVar 2 will deal with the genre radiobuttons 
    radioVar2 = tkinter.IntVar(recToplvl)
    radioVar2.set(5)


    #create Radiobuttons
    rb1 = tkinter.Radiobutton(ageRatingFrame,
                              text = "Young Adult/Teen",
                              variable = radioVar1,
                              value = 1)
                            #the arguement variable = radioVar, associates the
                            #Radiobutton with the radioVar object.
                            #the arguement value = 1 assigns the integer 1 to
                            #this specific radiobutton (rb1).
                            #Consquently, any time this Radiobutton is selected,
                            #the value 1 will be stored in the radioVar object.

    rb2 = tkinter.Radiobutton(ageRatingFrame,
                              text = "New Adult/Adult",
                              variable = radioVar1,
                              value = 2)
                            
    rb5 = tkinter.Radiobutton(genreFrame,
                              text = "Fantasy/Science Fiction",
                              variable = radioVar2,
                              value = 5)

    rb6 = tkinter.Radiobutton(genreFrame,
                              text = "Romance/Lighthearted",
                              variable = radioVar2,
                              value = 6)
    
    rb7 = tkinter.Radiobutton(genreFrame,
                              text = "Mystery/Thriller",
                              variable = radioVar2,
                              value = 7)

    #----------BUTTON FRAME-------------#
    #the showChoice() function is the callback function for the
    #OKButton. When the method/function executes, it calls the
    #radioVar object's get method to retrieve the value stored in the
    #object. Then it determines which values are selected and based
    #off of that it will give a reccomendation.
    #We call the showChoice() function before we create our OKButton widget
    def showChoice():

        #Create arrays for the message output  
        youngAdult= ["Throne of Glass \nby Sarah J. Maas",
                     "Better Than The Movies \nby Lynn Painter",
                     "A Good Girl's Guide To Murder \nby Holly Jackson"]
        adult = ["The Poppy War \nby R.F. Kuang",
                 "Happy Place \nby Emily Henry",
                 "Murder on the Orient Express \nby Agatha Christie"]

        #When it finds the user input to
        #a message output, then it will
        #turn the found to True, which
        #will break the loop 
        found = False

        #to check for every combination, we need to
        #create a nested loop. The outer loop will
        #deal with the ageRating radiobuttons as in the young adult 
        #and adult radiobuttons.  
        for g in range(2):

            #when found is equal to false, the inner loop
            #will continue running, otherwise it will break
            #and stop 
            if found == False:
                
                #the inner for loop will deal with the genre
                #of each young adult or adult selection.
                #Since we have 3 types of radiobuttons
                #(fantasy, romance and mystery)
                #the for loop needs to iterate 3 times.  
                for i in range(3):

                    #this will check to see which length
                    #radiobutton is checked. For example,
                    #if the first length radio button is checked
                    #it will have a value of 5 which is the
                    #i + 5 (i starts at a value of 0)
                    #however if it doesn't have a value of 5
                    #it will go back to the for loop and go
                    #to the next iteration which will make
                    #i equal to 1. This process will continue
                    #until the if statement is true 
                    if radioVar2.get() == i+5:

                        #this will check to see which genre
                        #is checked. For example, if the fantasy
                        #is checked, then it will show the
                        #choices for fantasy and length.
                        #Since fantasy has a value of 1, this
                        #will show the fantasy array. 
                        if radioVar1.get() == 1:

                            #show which reccomendation in a messagebox
                            #youngAdult[i] -- when the loop is running,
                            #it will run until it matches the if statement
                            #above. For example, if the first length option
                            #is selected then i will have a value of 0
                            #youngAdult is an array we assigned earlier and each
                            #item inside corresponds to a number placement
                            #the first item has a number value of 0
                            #so if the i is equal to 0, it will show the
                            #first item in the array. 
                            tkinter.messagebox.showinfo("Selection",
                                                        youngAdult[i])

                            #since we have found a match, we will change the
                            #value of found to True so that our if statement
                            #no longer works 
                            found = True

                            #https://www.w3schools.com/js/js_break.asp
                            #the statement is used to jump out of a loop
                            #so that it doesn't keep running
                            #We are using the break statement here because
                            #we don't want the for loop to run
                            #since it has already found the match
                            #Otherwise, it will run 3 times until
                            #the loop is finishes and then it will go to the
                            #outerloop.
                            break
                        
                        #This is the same concept as the fantasy one except
                        #it is selecting the second radiobutton genre which
                        #is romance. It follows the same principles. 
                        elif radioVar1.get() == 2:
                            tkinter.messagebox.showinfo("Selection", adult[i])
                            found = True
                            break
            
        

    #create the OKButton
    OKButton = tkinter.Button(buttonFrame,
                              text = "OK",
                              bg = "#374d5d",
                              fg = "White",
                              command = showChoice)

    #create quit button
    quitButton = tkinter.Button(buttonFrame,
                                text = "Quit",
                                bg = "White",
                                fg = "#374d5d",
                                command = recToplvl.destroy)

    #---PACK WIDGETS---#
    #radiobuttons
    rb1.pack()
    rb2.pack()
   
    rb5.pack()
    rb6.pack()
    rb7.pack()


    #buttonFrame
    OKButton.pack(side = "left")
    quitButton.pack(side = "left")
    

    #MAINLOOP
    recToplvl.mainloop()








