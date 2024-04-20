# from tkinter import *
# root = Tk()
# root.geometry('500x150')
# root.title("First GUI Application")
# root.resizable(width=True, height=True)

# Label(root, text="Hello From BD").pack()

# btn1 = Button(root,text="Increase")
# btn1.pack()
# btn2 = Button(root,text="Decrease")
# btn2.pack()

# root.mainloop()


# from tkinter import *
# class MyApplication(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Event Handling")
#         self.label1 = Label(self,text="0")
#         self.label1.pack()
#         self.btn1 = Button(self,text="Increase")
#         self.btn1.pack()
#         self.btn2 = Button(self,text="Decrease")
#         self.btn2.pack()

#         def clicked1(event):
#             self.label1.config(text= int(self.label1['text'])+1)

#         self.btn1.bind('<Button-1>', clicked1)

# if __name__ == "__main__":
#     myApp = MyApplication()
#     myApp.geometry('350x150')
#     myApp.mainloop()


# from tkinter import *
# class MyApplication(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Event Handling")
#         self.label1 = Label(self,text="I am a Label 1",fg="red",
#         bg = "teal")
#         self.label1.place(x=30,y=10,width=120,height=50)
#         self.label2 = Label(self,text="I am a Label 2",
#         font="Times 12 italic",bg = "cyan")
#         self.label2.place(x=30,y=40,width=120,height=25)
#         self.label3 = Label(self,text="I am a Label 3",bg = "yellow")
#         self.label3.place(x=30,y=70,width=120,height=25)

# if __name__ == "__main__":
#     myApp = MyApplication()
#     myApp.geometry("200x100")
#     myApp.mainloop()

from tkinter import *
class MyApplication(Tk):
    def __init__(self):
        super().__init__()
        self.title("Event Handling")
        for i in range(1,10):
            Button(self,text=i).grid(row=(i-1)//3,column=(i-1)%3)
if __name__ == "__main__":
    myApp = MyApplication()
    myApp.geometry("200x100")
    myApp.mainloop()
