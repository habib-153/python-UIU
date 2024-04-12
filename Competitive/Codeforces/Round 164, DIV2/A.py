t = int(input())
lst = []
for i in range(t):
    n, m , k = map(int, input().split())
    if m > k:
        lst.append("YES")
    else:
        lst.append("NO")
for j in lst:
    print(j)

# wrong ans on test case 2