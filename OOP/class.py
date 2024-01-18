class my_calculator:
    def product(self,*nums):
    # def product(self,num1, num2):
        # print(num1*num2)
        sum = 1
        for i in nums:
            sum= sum*i
        print(sum)

#  same name er method but different number of parameter -- > method overloading
c1 = my_calculator()
c1.product(4,5)
c1.product(4,3,5)