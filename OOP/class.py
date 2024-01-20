class my_calculator:
    def product(self,*nums):
    # def product(self,num1, num2):
        # print(num1*num2)
        sum = 1
        for i in nums:
            sum= sum*i
        print(sum)

# @dispatch(int, int, int) --> Another option for fixing method overloading
#  same name er method but different number of parameter -- > method overloading
c1 = my_calculator()
# c1.product(4,5)
# c1.product(4,3,5)

# ============================ constructor Overloading==========

class Student:
    # def __init__(self, name, id):
    #     self.name = name
    #     self.id = id
    def __init__(self, name, id, cg):
        self.name = name
        self.id = id
        self.cg = cg

# c1 = Student("carel", 22)
c2 = Student("Ab", 33, 4)