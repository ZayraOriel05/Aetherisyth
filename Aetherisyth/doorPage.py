#Import modules
import tkinter
import tkinter.messagebox 
import random

'''
The pupose of this program is to
create a window where users can enter
in answers after seeing a question
that is related to the Book of the
Month Game. A question will appear
and users have to enter in the right
answer to the question or else the
next question will not appear.
After they answer all the questions
correctly, the Book of the Month
will be revealed. Afterwards, they
can exit. 
'''

#make an array that holds all the questions 
questionsArray = ["What is the name of the Author?",
                  "How many pages does this book have?",
                  "What is the genre?",
                  "A book that sells over 100 million" + 
                  "\ncopies is known as a?",
                  "How many awards has this book won?", ""]

#make an array that holds all the answers to
#the questions
answersArray = ["Suzanne Collins", "384",
                "Dystopian", "Bestseller",
                "28", ""]

#create a variable that sets the score to zero 
score = 0

#set i to zero. In this case, i is used
#for the position of the array. For example
#the first item in an array has a value of 0
#and here we are setting i to 0. We can change
#the value of i later on to get different
#positions in the array. 
i = 0

#define the enterClues function 
#this is the code that drives the whole GUI
def enterClues():

    #globalize all thinngs needed 
    global timeLabel
    global entryBox
    global label
    global scoreLabel
    global score 
    global i
    
    #TOP LEVEL WINDOW   
    doorToplvl = tkinter.Toplevel()
    doorToplvl.title("Enter Clues")
    doorToplvl.geometry("400x275")
    
    #add instructional label - this gives
    #instructions on what to do.
    instructionsLabel = tkinter.Label(doorToplvl,
                                      text = "Enter the Answer to Your" +
                                      " \nClue as the questions come up." +
                                      " \nIf you answer all of them correctly," +
                                      " \nThe Book of the Month will be" +
                                      " \nrevealed.",
                                      font = ("Times New Roman", 12))
    #pack
    instructionsLabel.pack()

    #Add score label - this keeps track
    #of the score/how many questions the
    #user has entered correctly 
    scoreLabel = tkinter.Label(doorToplvl,
                               text = "Score: 0", 
                               font = ("Times New Roman", 12))

    #pack
    scoreLabel.pack()

    #Add a label to display the questions
    label = tkinter.Label(doorToplvl, font = ("Times New Roman", 18))
    label.pack()

    #add an entry widget so I can type in the
    #answers to the questions 
    entryBox = tkinter.Entry(doorToplvl)
    entryBox.pack()

    #Add an exit button
    exitButton = tkinter.Button(doorToplvl, text = "Exit",
                                font = ("Times New Roman", 14),
                                command = doorToplvl.destroy)
    #pack
    exitButton.pack()

    
    #configure and change the questions
    #label to correspond to string inside
    #the questionsArray based on the value
    #of i 
    label.config(text = (questionsArray[i]))

    
    #Set the focus on the entry box
    entryBox.focus_set()

    #bind the enter key to the
    #get_entry_value function 
    doorToplvl.bind("<Return>", get_entry_value)

   
###----------CALLBACK FUNCTION FOR MAIN-----------####
#This function takes input from the user and
#compares the answer to the answerArray. If the
#answer matches the one in the array, the score will be
#upated by adding 1 point. Once the score reaches 5,
#the book of the month will be revealed. This also
#provides the next Question to be displayed. 
def get_entry_value(event):

    #global all things needed 
    global value
    global answerArray
    global entryBox
    global score
    global i
    global questionArray

    #assign the input to a value 
    value = entryBox.get()

    #check to see if the value matches
    #with the answer in the positions
    #of i 
    if  value.lower()== answersArray[i].lower():

            #Update the score - increase by 1 
            score+=1

            #configure and change the score
            #label to show the new score 
            scoreLabel.config(text = "Score: " + str(score))

            #increase the value of i by 1 so
            #the next position in the arrays
            #are used. For example the questionArray
            #will show the next position question
            #and the answerArray will compare
            #the user input to the next position
            #answer.
            i += 1 

    #since we have 5 questions, if the user
    #answers all questions correctly, the
    #score will be equal to 5 and we can
    #reveal the book of the month
    if score == 5:

            #use the message box to show the answer 
            tkinter.messagebox.showinfo("Book of the Month",
                           "Congratulations! You got it right and opened" +
                           "\nthe door."
                           "\nThe Book of the Month is:" +
                           "\n\tThe Hunger Games by Suzanne Collins")

    #this clears the input text 
    entryBox.delete(0, tkinter.END)

    #configure and change the question
    #to match with the new position of i
    #basically shows the next question
    #in the array.
    label.config(text = (questionsArray[i]))
    
