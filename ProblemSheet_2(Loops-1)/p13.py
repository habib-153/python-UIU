# rows = int(input())
# for row in range(1, rows+1):
#     for col in range(1, rows*2):
#         if(row == rows or row+col == rows+1 or col-row== rows-1):
#             print("*", end='')
#         else:
#             print(end=' ')
#     print()










N = int(input())
for i in range(1, N+1):
    for j in range(1,N*2):
        if(i == N or i+j == N+1 or j-i == N-1):
            print("*", end="")
        else:
            print(end=' ')
    print()