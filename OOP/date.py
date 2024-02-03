import copy
class Date:
    """
        Hello WOrld. this is a doc string comment
    """
    def __init__(self,day=0,month=0,year=0):
        self.day=day
        self.month = month
        self.year = year
    @staticmethod
    def isLeapYear(year):
        return True
    
    @classmethod
    def whichMonth(cls,month):
        months = ["January","February","March",
                  "April","May","June",
                  "July","August","September",
                  "October","November","December"] 
        
        d = cls(12,3,2014)
        print(d)
        return months[month-1]
    def __del__(self):
        print("This is a destructor")
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
class Period:
    def __init__(self,start,end):
        self.start=copy.deepcopy(start)
        self.end = copy.deepcopy(end)
    def __str__(self):
        return f"{self.start} - {self.end}"

d1 = Date(31,1,2024)
d2 = Date(31,5,2024)

print(d1)
print(d2)
p = Period(d1,d2)
print(p)

d1.year=2025
print(d1)
print(p)
#del d1
#print(d1)
print(Date.isLeapYear(2000))
print(Date.whichMonth(2))