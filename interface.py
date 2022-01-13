from tkinter import *
from tkinter import font
# python script showing battery details
import psutil
import os
import  datetime
import wikipedia
import bonggoQuery
from tkinter import messagebox




# function returning time in hh:mm:ss
def convertTime(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	return "%d:%02d:%02d" % (hours, minutes, seconds)

# returns a tuple
battery = psutil.sensors_battery()
percentage= battery.percent
stauts =battery.power_plugged

if stauts==False:
    data = "unplaged"
else:
    data="plugged"
    
remaining_time =convertTime(battery.secsleft)
# print("Battery percentage : ", battery.percent)
# print("Power plugged in : ", battery.power_plugged)

# converting seconds to hh:mm:ss
# print("Battery left : ", convertTime(battery.secsleft))


root =Tk()
root.title("Secure Environment")
root.configure(bg="grey")
root.geometry("500x500")

# ADDING FUNCTIONS
# def all():
#     import all
query = StringVar()
user = StringVar()
password = StringVar()

# SECURITY CHECKING


 
# =================================================         
def search():
    query1 = query.get()
    # result = wikipedia.summary(f"{query1}", sentences = 2)
    # print(result)
    bonggoQuery.speak("Please use the JArvis here!")
    query.set("Please use the JArvis here!")

def Off():
    root.destroy()

def explorer():
    
    os.startfile("filemanager.py")

def clock():
    
    os.startfile("clock.py")

def calculator():
   
    os.startfile("calculator.py")
    
def browser():
    
    os.startfile("Browser.py")
 
def texteditor():
   
    os.startfile("texteditor.py")
    
def ai():
   os.startfile("ai.py")

def weather():
    bonggoQuery.Query.normal_query.speaking("weather report")

def media():
    os.startfile("mediaPlayer.py")
# USING BACKGROUND

bg = PhotoImage(file = "5.png")
Label(image=bg).place(x=0, y=0)
# ----------------------------------------

Label(root, text="welcome to secure Environment", font="lucida 25 bold").pack()
Label(root, text="We are here to provide a strong secure environment to you! and also going to give a speacial features to the users! :)").pack(pady=10)
c = Canvas(root, bg="white", height=10)
c.pack()



f = Frame(root,bg="white")
f.pack(anchor="sw", side=BOTTOM, pady=2)

# Label(f, text="Hello").pack()


# ALL aPP
Button(f, text="AI", command=ai).pack(side=LEFT, padx=10)

# -------------------------------

Entry(f, width=50,textvariable=query).pack(side=LEFT, padx=10)
Button(f, text="Search", command=search).pack(side=LEFT, padx=10)

Button(f, text="Text Editor", command=texteditor).pack(side=LEFT, padx=10)
Button(f, text="Browser", command=browser).pack(side=LEFT, padx=10)
Button(f, text="Calculator", command=calculator).pack(side=LEFT, padx=10)
Button(f, text="Clock", command=clock).pack(side=LEFT, padx=10)
Button(f, text="Explorer",command=explorer).pack(side=LEFT, padx=10)
Button(f, text="Media Player", command=media).pack(side=LEFT, padx=10)

# ADDING BATTERY PERCENTAGE
Label(f,text=f"Battery: {percentage}%").pack(side=LEFT)
Label(f,text=data).pack(side=LEFT)
Label(f,text=f"Remaining Time: {remaining_time}").pack(side=LEFT)
# ---------------------------------------------------------

Button(f, text="Weather", command=weather).pack(side=LEFT, padx=10)


# DATE TIME
full_data =str(datetime.datetime.now())
mod_data = full_data.split(" ")
date = mod_data[0]
time = mod_data[1]
accurate_time = time.split(".")

Label(f,text=f"{date}\n{accurate_time[0]}").pack(side=LEFT)

# -------------------------------------------
Button(f, text="off", command=Off).pack(side=LEFT, padx=10)


root.mainloop()