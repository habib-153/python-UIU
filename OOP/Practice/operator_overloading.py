class data:
    def __init__(self,x):
        self.x = x
    def __add__(self, other):
        return self.x + other.x


num1 = data(10)
num2 = data(20)
str1 = data("DS")
str2 = data("UIU")
print(str1+str2)