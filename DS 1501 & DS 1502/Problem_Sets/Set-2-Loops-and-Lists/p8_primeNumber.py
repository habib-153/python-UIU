# check a number whether a prime number or not
num = int(input())
if num == 1:
    print('Not Prime')
for i in range(2, num):
    if num%i == 0:
        print("Not Prime")
        break
    else:
        print("Prime")
        break


# print the prime numbers in specific range
# start = int(input())
# end = int(input())
# for num in range(start, end+1):
#     if num > 1:
#         for i in range(2, num):
#             if num%i == 0:
#                 break
#         else:
#             print(num, end=' ')
