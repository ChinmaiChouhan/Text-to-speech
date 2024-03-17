"""import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Combobox
import pyttsx3
import os

root = tk.Tk()
root.title("Text To Speech")
root.geometry("400x400 ")
root.resizable(False,False)
root.configure(bg="#305065")

#icon
#image_icon = PhotoImage(file=" mic")
#root.iconphoto(False , image_icon)

#Top Frame
Top_frame = Frame(root , bg="white" , width=900 , height = 100)
Top_frame.place(x=0 ,y=0)

Logo = PhotoImage(file=" ")
Label(Top_frame , image= Logo , bg="white").place(x=10,y=5)

root.mainloop()"""
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Combobox
import pyttsx3
import os
#import pywin32


root = tk.Tk()
root.title("Text To Speech")
root.geometry("900x450")  # Remove the extra space here
root.resizable(False, False)
root.configure(bg="#305065")


engine = pyttsx3.init()

def speaknow():
    text= text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()

        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()


    if (text):
        if(speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()

        elif(speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()

        else:
            engine.setProperty('rate', 60 )
            setvoice()

def download():
    text= text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text , 'text.mp3')
            engine.runAndWait()


    if (text):
        if(speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()

        elif(speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()

        else:
            engine.setProperty('rate', 60 )
            setvoice()
    
            
#icon
root.iconbitmap("C:/Users/dell/AppData/Local/Programs/Python/Python312/icons8-speak-50.png")
#image_icon = PhotoImage(file=" C:/Users/dell/AppData/Local/Programs/Python/Python312/icons8-mic-50.png")
#root.iconphoto(False , image_icon)

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="C:/Users/dell/AppData/Local/Programs/Python/Python312/icons8-mic-50.png ")
Label(Top_frame, image=Logo, bg="white").place(x=5, y=2)
Label(Top_frame , text="TEXT TO SPEECH" , font="arial 20 bold" , bg="white" , fg="black").place(x=80, y=15)

#text area
text_area=Text(root,font="Robote 20" , bg="white" , relief=GROOVE , wrap=WORD)
text_area.place(x=10 , y=150,width=500,height=250)

Label(root , text="VOICE" , font="arial 20 bold" , bg="#305065" , fg="white").place(x=550, y=160)
gender_combobox = Combobox(root,values=['Male' , 'Female'] , font="arial 14" , state='r' , width=10)
gender_combobox.place(x=550 , y=200)
gender_combobox.set('Male')


Label(root , text="SPEED" , font="arial 20 bold" , bg="#305065" , fg="white").place(x=730, y=160)
speed_combobox = Combobox(root,values=['Fast' , 'Normal', 'Slow'] , font="arial 14" , state='r' , width=10)
speed_combobox.place(x=730 , y=200)
speed_combobox.set('Normal')


imageicon = PhotoImage(file="C:/Users/dell/AppData/Local/Programs/Python/Python312/icons8-speak-50.png")
btn = Button(root,text="Speech",compound = LEFT,image = imageicon ,width=130 , font="arial 14 bold", command = speaknow)
btn.place(x=550 , y=280)

imageicon2 = PhotoImage(file="C:/Users/dell/AppData/Local/Programs/Python/Python312/icons8-download-24.png")
save = Button(root,text="Save",compound = LEFT,image = imageicon2 ,width=165,height=50,bg="#39c790" , font="arial 14 bold" ,command=download)
save.place(x=710 , y=280)
root.mainloop()


