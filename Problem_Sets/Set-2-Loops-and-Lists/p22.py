A = []
print("Enter Matrix A: ")
for i in range(2):
    a = list(map(int, input().split()))

    A.append(a)

B = []
print("Enter Matrix B: ")
for i in range(3):
    b = list(map(int, input().split()))
    B.append(b)

C = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(3):
            C[i][j] += A[i][k] * B[k][j]
print()
# Print the resulting matrix C
for row in C:
    for r in row:
        print(r, end=' ')
    print()