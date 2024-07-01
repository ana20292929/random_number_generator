import tkinter as tk
import random
from tkinter import Button, Entry, Label, Text, END

#generated a random number in a certain range
def showRandNum():
    resultText.delete('1.0', END) #clear text
    try:
        fromVal = int(rangeMin.get())
        toVal = int(rangeMax.get())

        if(fromVal > toVal): #if from > to
            resultText.insert(END, "Invalid range. The 'From' value must be less than the 'To' value.")
            return
        
        #if the input is valid
        finalNum = random.randint(fromVal, toVal) #generate random number
        resultText.insert(END, finalNum) #display
        submitNum.destroy() #clear the submit button because a number was generated
    except ValueError:
        resultText.insert(END, "Invalid Input. Please enter integers.") #if integer isn't entered


#Create window
root = tk.Tk()
root.title('Random Number Generator')
root.geometry("300x250")

#show text
rangeText = Label(root, text='Enter your range for the number generator')
rangeText.grid(row=0, columnspan=2)

#Set up range labels and entry fields
Label(root, text='From').grid(row=1)
Label(root, text='To').grid(row=2)
rangeMin = Entry(root)
rangeMax = Entry(root)
rangeMin.grid(row=1, column=1)
rangeMax.grid(row=2, column=1)

#button to submit the numbers
submitNum = Button(root, text="Submit", command=showRandNum)
submitNum.grid(row=3, column=1)

#text where the result or invalid input message is displayed
resultText = Text(root, height=10, width=20, wrap='word') #there is wrap for the message to be neater
resultText.grid(row=4, column=1)

root.mainloop()