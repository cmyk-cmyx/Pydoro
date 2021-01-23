from tkinter import Tk, Button, DISABLED, Label, ACTIVE
import time
from plyer.utils import platform
from plyer import notification

#main window configuration
root = Tk()
root.title ("PyDoro")
root.geometry ("400x400")
root.configure(bg = "#383838") 

#colours for the text
Colour1 = "#c4c4c4"
Colour2 = "#292828"

def Date(): #Defines the date for displaying under the clock
    day = time.strftime("%d")
    month = time.strftime("%b") # %B can be used for full month
    year = time.strftime("%Y")

    Calendar.config (text= day + " " + month + " " + year)

def clock(): # for creating the clock
    tizo = time.strftime("%X") #Find the time for your locale
    Time.config (text = tizo)
    Time.after (1000, clock)
    Date() #calling the Date because it makes sense to do it here

def Stop():
    print ("nothing")

def Start():
    time_left = (55) #40-60 minutes of work
    Stop.config (state = ACTIVE)
    timer = Label (root, text = time_left)
    timer.pack()
    def update(time_left):
        timer["text"] = time_left
        if time_left > 0:
            root.after(60000, update, time_left-1) # Wait 60000ms or 1 minute
        # elif 
    update(time_left)
        


Start = Button (root, text = "Start!", fg = Colour1, bg = Colour2, padx = 40, command = Start)
Stop = Button (root, text = "stop", fg = Colour1, bg = Colour2, state = DISABLED)

Time = Label (root, text="", font = ("Helvetica", 50), fg = Colour1, bg = "#383838")
Time.pack (pady = 5)

Calendar = Label (root, font = ("Helvetica", 12), fg = Colour1, bg = "#383838")
Calendar.pack (pady = 5)

Start.pack (pady = 10)

Stop.pack (pady = 10)


clock()
root.mainloop() #Runs the program