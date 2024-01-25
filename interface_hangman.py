from tkinter import *

fenetre = Tk()
fenetre.minsize(500,500)
fenetre.title("Hangman game")

bouton_quitter = Button(fenetre, text = "Quitter", command = fenetre.quit)
bouton_quitter.pack()

fenetre.mainloop()