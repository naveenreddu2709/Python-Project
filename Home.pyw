from tkinter import *
import os
import subprocess
from time import *
from PIL import Image, ImageTk

# function according to their need
def cal():
    runcal=path2("Calculater.pyw")
    subprocess.Popen(["python", f"{runcal}"])
    SystemExit
def snake():
    snake=path2("snake.pyw")
    subprocess.Popen(["python", f"{snake}"])
def clear():
    tc=path2("Clear_temp.py")
    subprocess.Popen(["python", f"{tc}"])

def quiz():
    quiz_=path2("Quiz.pyw")
    subprocess.Popen(["python", f"{quiz_}"])

root=Tk()
# Set the screen size
screen_width=900
screen_height=600
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False,False)

# getting the path of the files
script_dir = os.path.dirname(os.path.abspath(__file__))

def path(pth):
    return os.path.join(script_dir,f"images\{pth}")
def path2(pth):
    return os.path.join(script_dir,f"{pth}")

# update time
def updatetime():
    tim = strftime("%I:%M:%S %p")
    clock.config(text=tim)
    weekday=strftime("%A")
    mnth=strftime("%B")
    dat=strftime(r"%d")
    day.config(text=f"{weekday[:3]}, {dat} {mnth[:3]}")
    root.after(1000,updatetime)

# changeing the icon
root.title("Voxie")
try:
    icn = path("12.ico")
    root.wm_iconbitmap(icn)
except:
    pass

# backgound image
root.config(bg="black")
backg = path("main.jpg")
backimg= ImageTk.PhotoImage(Image.open(backg))
Label(image=backimg).place(x=0,y=0,relheight=1,relwidth=1)

# Clock
clockfrm = Frame(borderwidth=10,relief=SUNKEN,bg="blue")
clockfrm.place(x=150,y=100,width=180,height=90)
clock = Label(clockfrm,text="hello",font="comicansms 20 bold",fg="white",bg="black",width=180)
clock.pack()
day = Label(clockfrm,text="world",font="Harrington 20 bold",fg="black",bg="white",width=180)
day.pack()
updatetime()

# options like apps
calimg = PhotoImage(file=path("cal.png"),width=80,height=80)
but=Button(root,image=calimg,bg="black",borderwidth=0,activebackground="black",command=cal)
but.place(x=100,y=(screen_height-150))
snkimg = PhotoImage(file=path("snk.png"),width=80,height=80)
but1=Button(root,image=snkimg,bg="black",borderwidth=0,activebackground="black",command=snake)
but1.place(x=250,y=(screen_height-150))
quimg = PhotoImage(file=path("quiz.png"),width=80,height=80)
but2=Button(root,image=quimg,bg="black",borderwidth=0,activebackground="black",command=quiz)
but2.place(x=500,y=(screen_height-150))
tfcimg = PhotoImage(file=path("tfc.png"),width=80,height=80)
but4=Button(root,image=tfcimg,bg="black",borderwidth=0,activebackground="black",command=clear)
but4.place(x=650,y=(screen_height-150))

root.mainloop()