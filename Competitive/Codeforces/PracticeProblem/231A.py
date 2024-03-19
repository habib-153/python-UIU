n = int(input())
matrix = []

for i in range(n):
    lst = list(map(int, input().split()[:3]))
    matrix.append(lst)
# print(matrix)
count = 0
for i in matrix:
    c=0
    for j in i:
        if j == 1:
            c += 1
    if c>=2:
        count += 1
print(count)