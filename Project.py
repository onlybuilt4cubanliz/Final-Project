import os
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3
from tkinter import *

root = Tk()
root.title("Music Manager")
root.minsize(400,400)


songs = []
names = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

index = 0

def chooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            names.append(audio['TIT2'].text[0])


            songs.append(files)




chooser()



def call(event):
    k=chooser()


    names.reverse()

    songlabel.pack()

def rem(event):
    listbox.delete(0)

def closewindow():
    exit()

button = Button(text="Quit",command = exit )
menu=Menu()
root.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=subMenu)
subMenu.add_command(label="Quit",command=closewindow)


label = Label(root,text='Songs')
label.pack()

listbox = Listbox(root,selectmode=MULTIPLE,height=45,width=20)
listbox.pack(fill=X)

songs.reverse()
names.reverse()

for items in names:
    listbox.insert(0,items)

names.reverse()
songs.reverse()

framedown =Frame(root)
framedown.pack()


rembutton=Button(root,text ='Remove Songs/List')
rembutton.pack(side=RIGHT)
openbutton=Button(root,text ='Open')
openbutton.pack(side=LEFT)




rembutton.bind("<Button-1>",rem)
openbutton.bind("<Button-1>",call)



songlabel.pack(side=TOP)













root.mainloop()

