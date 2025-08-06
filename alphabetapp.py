import tkinter 
import pygame
from PIL import Image,ImageTk
import string
import random
#window config 
window = tkinter.Tk()
window.geometry("800x500")
window.resizable(False,False)
window.title("A-Z")

backgroundimageopen = Image.open("759404.jpg")
chnagebackgroundimage = ImageTk.PhotoImage(backgroundimageopen)
backgroundlabel = tkinter.Label(window,image=chnagebackgroundimage,width=800,height=500)
backgroundlabel.place(x=0, y=0, relwidth=1, relheight=1)


pygame.mixer.init()

def play_sound(letter):
    pygame.mixer.music.load(f"{letter.lower()}.mp3")
    pygame.mixer.music.play(loops=0)

colorlist = [ "red", "orange", "yellow", "green", "blue", "purple",
    "pink", "cyan", "magenta", "lime", "gold", "skyblue",
    "salmon", "violet", "lightgreen", "turquoise", "orchid",
    "tomato", "plum", "wheat", "khaki", "coral", "navy", "olive",
    "teal", "maroon"
    ]


row = 0
col = 0
for letter in string.ascii_uppercase:
    randomcolor = random.choice(colorlist)
    btn = tkinter.Button(
        window,
        text=letter,
        width=10,
        height=5,
        bg= randomcolor,
        command=lambda l=letter: play_sound(l)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 9: 
        col = 0
        row += 1



window.mainloop()