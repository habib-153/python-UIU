num = int(input())

for i in range(1, num + 1):
    # for printing space before the number
    print(" " * (num - i), end="")
    #ascending order from 1 to i
    for j in range(1, i + 1):
        print(j, end="")
    #descending order from i - 1 to 1
    for k in range(i - 1, 0, -1):
        print(k, end="")
    # Print a new line
    print()

for i in range(num - 1, 0, -1):
    # for printing space before the number 
    print(" " * (num - i), end="")
    # Print the numbers in ascending order from 1 to i
    for j in range(1, i + 1):
        print(j, end="")
    # Print the numbers in descending order from i - 1 to 1
    for k in range(i - 1, 0, -1):
        print(k, end="")
    # Print a new line
    print()
