from tkinter import Tk, Button, DISABLED, Label, ACTIVE, BOTTOM
import time
from plyer.utils import platform
from plyer import notification

#main window configuration
root = Tk()
root.title ("PyDoro")
root.geometry ("400x400")
root.configure(bg = "#383838")

#colours for the text
Colour1 = "#c4c4c4" #Light gray
Colour2 = "#292828" #Dark Gray
Colour3 = "#ffccfa" #Pink
Colour4 = "#e62727" #Red

running = True

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
    Start.config (state = ACTIVE)
    Stop.config (state = DISABLED)
    global running
    running = False

def Timer2():
    time_left = (22) #Whatever length you want the break to be
    timer = Label (root, font = ("helvetice", 30), fg = Colour3, bg = "#383838", text = time_left)
    timer.pack()

    def update(time_left):
        timer["text"] = time_left
        if running:
            if time_left > 0:
                root.after(60000, update, time_left-1) # Wait 60000ms or 1 minute

            if time_left == 0:
                notification.notify (title = "Break over", message = "Time to get back to work." , app_name='Animedoro',)
                Start.update()
                timer.pack_forget()
        else:
            timer.pack_forget()
            pass
            Start    

    update(time_left)
    global running
    running = True

#This is what happens when you press the start button
def Start():

    time_left = (45) #40-60 minutes of work
    Start.config (state = DISABLED)
    Stop.config (state = ACTIVE)
    timer = Label (root, font = ("helvetice", 30), fg = Colour4, bg = "#383838", text = time_left)
    timer.pack()

    def update(time_left):
        timer["text"] = time_left
        if running:
            if time_left > 0:
                root.after(60000, update, time_left-1) # Wait 60000ms or 1 minute

            if time_left == 0:
                notification.notify (title = "Timer over", message = "Time to have a break!" , app_name='Animedoro',)
                timer.pack_forget()
                Timer2() #Go to the second (break) timer if time gets to 0 without stop being pressed
        else:
            timer.pack_forget()
            pass
            Start

    update(time_left)
    global running
    running = True
        

Start = Button (root, text = "Start!", fg = Colour1, bg = Colour2, padx = 40, command = Start)
Stop = Button (root, text = "stop", fg = Colour1, bg = Colour2, state = DISABLED, command = Stop)

Time = Label (root, text="", font = ("Helvetica", 45), fg = Colour1, bg = "#383838")
Time.pack (pady = 2)

Calendar = Label (root, font = ("Helvetica", 12), fg = Colour1, bg = "#383838")
Calendar.pack (pady = 5)

Start.pack (pady = 10)
Stop.pack (pady = 10, side = BOTTOM)


clock()
root.mainloop() #Starts the program