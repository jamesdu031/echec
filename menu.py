from Tkinter import *
from importlib import import_module

def Run():
    import_module("Echec")


fenetre = Tk()
tex1 = Label(fenetre, text='Bienvenue pour jouer aux ECHECS !!!', fg='black')
tex1.pack()
Run = Button(fenetre, text="Jouer", command=Run)
Run.pack(side=TOP)
quit_button = Button(fenetre, text='Quitter', command = fenetre.destroy)
quit_button.pack()
mainloop()
