num = int(input())

for i in range(1, num + 1):
    # for printing space before the number
    print(" " * (num - i), end="")
    for j in range(i, 0,-1):
        print(j, end="")
    for k in range(2,i+1):
        print(k, end="")
    # Print a new line
    print()

for i in range(num - 1, 0, -1):
    print(" " * (num - i), end="")
    for j in range(i, 0,-1):
        print(j, end="")
    for k in range(2,i+1):
        print(k, end="")
    # Print a new line
    print()
