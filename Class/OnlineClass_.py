# sum of all number which  are divisible 3 in 1-100
    # # sum = 0
    # # for i in range(1,101):
    # #     if i%3 == 0:
    # #         sum += i
    # # print(sum)

    # sum = 0
    # for i in range(3,101,3):
    #     sum += i
    # print(sum)

# print 50-1
    # for i in reversed(range(1,51)):
    #     print(i)

# reversed print
    # number = int(input())
    # for i in reversed(range(1,number+1)):
    #     print(i, end=' ')

# problem 3
    # N = int(input())

    # for i in range(1, N+1):
    #     if i%2 == 1:
    #         print('1', end='')
    #     else:
    #         print('0', end='')

# problem 4
    # n = int(input())
    # number = input().split()[:n]
    # sum = 0
    # for i in number:
    #     sum = sum + float(i)
    # avg = (sum / n)
    # print(f"Average: {avg}")

# problem 5--max

n= int(input())
max = float(input())
for i in range(0,n-1):
    num = float(input())
    if num > max:
        max = num
    
print(max)