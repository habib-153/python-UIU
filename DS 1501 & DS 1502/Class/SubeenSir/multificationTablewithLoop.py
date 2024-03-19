def multiplication_table(n):
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')
num = int(input("Enter a number (0 to exit): "))

while num!=0:
    multiplication_table(num)
    print("")
    num = int(input("Enter a number (0 to exit): "))
