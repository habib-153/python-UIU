# check a number whether a prime number or not
# num = int(input())
# if num == 1:
#     print('not a prime number')
# for i in range(2, num):
#     if num%i == 0:
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")


# print the prime numbers in specific range
start = int(input())
end = int(input())
for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num, end=' ')
