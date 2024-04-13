from tkinter import *

root = Tk()
root.title("Gui Demo Lab")

root.configure(background="blue")
imgobj = PhotoImage(file=r"C:\Users\hrsih\OneDrive\Pictures\Screenshots\Screenshot 2024-04-10 000413.png")

labe1 = Label(root, image=imgobj)
labe1.pack()

root.mainloop()

# from tkinter import Tk, Label
# from PIL import Image, ImageTk

# root = Tk()

# file = '/home/master/Work/Tensorflow/Project/Data/images/p001.png'

# image = Image.open(file)

# zoom = 1.8

# #multiple image size by zoom
# pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])

# img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y))) 
# label = Label(root, image=img)
# label.image = img
# label.pack()

# root.mainloop()