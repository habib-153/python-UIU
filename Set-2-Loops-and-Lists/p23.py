R = int(input())
C = int(input())
A=[]
for i in range(R):
    number_str = input().split()
    if(len(number_str) > C):
        print('Invalid Input')
        break
    else:
        numbers = [int (x) for x in number_str]
        A.append(numbers)
if(len(A)>0):
    for row in range(R):
        max_value = max(A[row])
        print(max_value)

# row = int(input())
# col = int(input())
# A = []
# for i in range(1,row+1):
#     number_str = input().split()
#     if(len(number_str) > col):
#         print('Invalid Input')
#         break
#     else:
#         numbers = [int (x) for x in number_str]
#         A.append(numbers)

