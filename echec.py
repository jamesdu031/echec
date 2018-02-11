# Créé par charlier, le 25/01/2018 en Python 3.2
from tkinter import *
import PIL.Image as Im

def click(event):
    print(event.x//92, event.y//86)

fenetre = Tk()
photo = PhotoImage(file="echiquier.gif", format="gif")
canvas = Canvas(fenetre,width=735, height=689)
canvas.create_image(0, 0, anchor=NW, image=photo)
piece = canvas.create_oval(0,0,92,86,fill="blue")
canvas.pack()
canvas.bind("<Button-1>", click)
fenetre.mainloop()





