from tkinter import *

root = Tk()
root.title("Gui Demo Lab")

root.configure(background="blue")
imgobj = PhotoImage(file=r"C:\Users\hrsih\OneDrive\Pictures\Screenshots\Screenshot 2024-03-04 220836.png")

labe1 = Label(root, image=imgobj)
labe1.pack()

root.mainloop()