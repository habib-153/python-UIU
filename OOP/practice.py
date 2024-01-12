class Student:
    def __init__(self, name,id):
        self.name = name
        self.id = id
    
    def details(self):
        #print("Name:",self.name,",ID:",self.id)
        Name = self.name
std1 = Student("Habibi", 12)
std1.details()

# variable = className()  --> ebhabe object create kore
# __init__ --> constructor --> object create kore dey

class Car:
    def __init__(self, name, model):
        self.name = name      #instance variable
        self.model = model
        self.wheel = 4
    def view(self):           # instance method
        print(self.name, self.wheel, self.model)

C1 = Car("BMW", 2016)
C2 = Car("Audi", 2017)

C1.view()
C2.view()