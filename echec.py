# Créé par charlier, le 25/01/2018 en Python 3.2
from tkinter import *
from time import sleep
import PIL.Image as Im



def clickx(event):
    return event.x

def clicky(event):
    return event.y

def oval(x,y):
    """affiche un cercle de coordonnéés x et y"""
    piece = canvas.create_oval(x,y,x+92,y+92,fill="blue")
    return piece

def souris(event):
    global coords
    if x<=clickx<=x+92:
        canvas.coords(pieceout, 100, 100, 100+92, 100+92)



fenetre = Tk()
photo = PhotoImage(file="echiquier2.gif", format="gif")
canvas = Canvas(fenetre,width=800, height=800)
canvas.create_image(0, 0, anchor=NW, image=photo)

canvas.pack()
canvas.bind("<Button-1>", clickx)


pieceout = oval(200,0)
canvas.focus_set()
canvas.bind("<Button-1>", souris)
fenetre.mainloop()










