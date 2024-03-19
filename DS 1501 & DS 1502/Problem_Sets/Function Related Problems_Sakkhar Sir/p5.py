def swap(a,b):
    a,b = b,a
    print(f"Value in func: {a} {b}")

num1 = int(input())
num2 = int(input())

swap(num1, num2)
print("value in main: ", num1, num2)