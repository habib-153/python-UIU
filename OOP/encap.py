
"""
--> we can use get set method...it is a naming convention.
--> __method ---> private method....class er bahire theke access kora jabe nah... we can also create private instance variable(__name)
-->
"""
class ABC:
    def __init__(self,name,id):
        self.name = name
        self.__id = id
    def details(self):
        print("Name:",self.name,"Id:",self.__id )
    def __method(self):
        print("private method executed")
s1 = ABC("Bob", 11)
s1.details()
# s1.__method()