from tkinter import *
import tkinter as tk
from tkinter import ttk ,filedialog
from pygame import mixer
import os 

root=Tk()
root.geometry("920x670+290+85")
root.config(bg="yellow")
root.resizable(False,False)

mixer.init()

def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play():
    music_name=playlist.get(ACTIVE)
    
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])


icon_photo=PhotoImage(file=\logo (1).png")
root.iconphoto(False,icon_photo)

top_photo=PhotoImage(file="top (2).png")
Label(root,image=top_photo,bg="yellow").pack()

logo_photo=PhotoImage(file="logo (1).png")
Label(root,image=logo_photo,bg="yellow").place(x=65,y=115)


play_button=PhotoImage(file="icons8-play-button-100.png")
Button(root,image=play_button,bg="yellow",bd=0,command=play).place(x=100,y=400)

stop_button=PhotoImage(file="icons8-stop-circled-100.png")
Button(root,image=stop_button,bg="yellow",bd=0,command=mixer.music.stop).place(x=210,y=500)

resume_button=PhotoImage(file="icons8-resume-button-100.png")
Button(root,image=resume_button,bg="yellow",bd=0,command=mixer.music.unpause).place(x=125,y=500)

pause_button=PhotoImage(file="icons8-pause-button-100.png")
Button(root,image=pause_button,bg="yellow",bd=0,command=mixer.music.pause).place(x=30,y=500)

music=Label(root,text="",font=("arial",15),fg="#0f1a2b",bg="yellow")
music.place(x=150,y=340,anchor="center")


menu=PhotoImage(file="Downloads\\menu.png")
Label(root,image=menu,bg="yellow",).pack(padx=10,pady=50,side=RIGHT)

musİc_Frame=Frame(root,bd=2,relief=RIDGE)
musİc_Frame.place(x=330,y=350,width=560,height=250)

Button(root,text="Open Folder",font=("arial",10,"bold"),width=15,height=2,fg="yellow",bg="#21b3de",command=open_folder).place(x=330,y=300)

scroll=Scrollbar(musİc_Frame)
playlist=Listbox(musİc_Frame,width=100,font=("arial",10),fg="grey",bg="#333333",selectbackground="lightblue",
                 cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)







root.mainloop()
