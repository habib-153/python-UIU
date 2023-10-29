R = int(input())
C = int(input())
A=[]
for i in range(R):
    list_str = input().split()[:C]
    list = [int (x) for x in list_str]
    A.append(list)
for row in range(R):
    max_value = max(A[row])
    print(max_value)