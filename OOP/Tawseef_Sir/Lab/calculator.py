from tkinter import *
class Calculator(Tk):
    def __init__(self):
        super().__init__()

        self.input_field = Entry(self, width=35, borderwidth=5) 
        self.input_field.grid(row=0, column=0, columnspan=3)

        self.bt_0 = Button(self, padx=40, pady=20, text='0')
        self.bt_1 = Button(self, padx=40, pady=20, text='1')
        self.bt_2 = Button(self, padx=40, pady=20, text='2')
        self.bt_3 = Button(self, padx=40, pady=20, text='3')
        self.bt_4 = Button(self, padx=40, pady=20, text='4')
        self.bt_5 = Button(self, padx=40, pady=20, text='5')
        self.bt_6 = Button(self, padx=40, pady=20, text='6')
        self.bt_7 = Button(self, padx=40, pady=20, text='7')
        self.bt_8 = Button(self, padx=40, pady=20, text='8')
        self.bt_9 = Button(self, padx=40, pady=20, text='9')

        self.btn_clear = Button(self, padx=75, pady=20, text='Clear')
        self.btn_add = Button(self, padx=40, pady=20, text='+')
        self.btn_sub = Button(self, padx=40, pady=20, text='-')
        self.btn_mul = Button(self, padx=40, pady=20, text='*')
        self.btn_div = Button(self, padx=40, pady=20, text='/')
        self.btn_eq = Button(self, padx=85, pady=20, text='=')

        # place the buttons
        self.bt_0.grid(row=4, column=0)
        self.btn_clear.grid(row=4, column=1, columnspan=2)

        self.bt_1.grid(row=1, column=0)
        self.bt_2.grid(row=1, column=1)
        self.bt_3.grid(row=1, column=2)

        self.bt_4.grid(row=2, column=0)
        self.bt_5.grid(row=2, column=1)
        self.bt_6.grid(row=2, column=2)

        self.bt_7.grid(row=3, column=0)
        self.bt_8.grid(row=3, column=1)
        self.bt_9.grid(row=3, column=2)

        self.btn_add.grid(row=5, column=0)
        self.btn_eq.grid(row=5, column=1 , columnspan=2)
        self.btn_sub.grid(row=6, column=0)
        self.btn_mul.grid(row=6, column=1)
        self.btn_div.grid(row=6, column=2)
    
    def take_input(self, number):
        current_value = self.input_field.get()
        self.input_field.delete(0, END)
        self.input_field.insert(current_value+str(number))
    def add(self):
        first_num = self.input_field.get()
        

if __name__ == "__main__":
    c= Calculator()
    c.mainloop()