class Vaccine:
    def __init__(self,name,md_in, interval):
        self.name = name
        self.md_in = md_in
        self.interval = interval

class Person:
    def __init__(self, name, age, ptype):
        self.name = name
        self.age = age
        self.ptype = ptype
        self.vac = ""
        self.firstDose = False
        self.secDose = False
    def pushVaccine(self, vaCn, dose='1st dose'):
        if dose == '1st dose':
            if self.age >= 25 or self.ptype == 'Student' or self.ptype == 'student' :
                self.vac=vaCn
                self.firstDose = True
                print("1st dose Done for", self.name)
            else:
                print("Sorry", self.name,". Minimum age for taking vaccine is 25")
        else:
            if self.vac.name != vaCn.name:
                print("Sorry", self.name, "You can't take two different vaccine")
            elif self.firstDose == True:
                self.secDose = True
                print("2nd dose done")
    
# ===========
astra = Vaccine("Astrazeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
Mahi = Person("Mahi", 18, "student")
Mahi.pushVaccine(sin)
print(Mahi.vac.name)