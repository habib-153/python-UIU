numbers = input()
num = numbers.split()

num1 = int(num[0])
num2 = int(num[1])

if(num1 > num2):
    y=num1
    x=num2
else:
    x=num1
    y=num2
for i in range(x, y+1):
    if x != y:
        print(i**2, end=" ")
print("END")
