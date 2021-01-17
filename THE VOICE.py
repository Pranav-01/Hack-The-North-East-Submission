#TEMP
import tkinter
from gtts import gTTS
import os

window = tkinter.Tk()

window.title("THE VOICE")

window.geometry("260x150")

l1 = tkinter.Label(window,text="MENU")
l1.grid(column=0,row=0)

txt = tkinter.Entry(window,width=36)
txt.grid(column=0,row=1)

def click11():
    res=txt.get()
    mytext=res
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("start welcome.mp3")

def click1():
    l1.configure(text="ENTER TEXT IN THE TEXTBOX")
    b1 = tkinter.Button(window,text="Enter",command=click11)
    b1.grid(column=1,row=1)

def click22():

    DIR=txt.get()
    f = open(DIR)
    mytext = f.read()
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("start welcome.mp3")

def click2():
    l1.configure(text="ENTER FILE DIRECTORY IN THE TEXTBOX")
    b1 = tkinter.Button(window,text="Enter",command=click22)
    b1.grid(column=1,row=1)

def click3():
    exit(0)

b2 = tkinter.Button(window,text="1. Text",command=click1)
b3 = tkinter.Button(window,text="2. File",command=click2)
b4 = tkinter.Button(window,text="3. Exit",command=click3)

b2.grid(column=0,row=3)
b3.grid(column=0,row=4)
b4.grid(column=0,row=5)

window.mainloop()
