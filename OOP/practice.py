class Student:
    def __init__(self, name,id):
        self.name = name
        self.id = id
    
    def details(self):
        print("Name:",self.name,",ID:",self.id)
std1 = Student("Habibi", 12)
std1.details()

# variable = className()  --> ebhabe object create kore
# __init__ --> constructor --> object create kore dey