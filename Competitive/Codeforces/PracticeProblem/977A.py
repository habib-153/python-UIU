n,k = map(int, input().split())
# print(n[-1])
for i in range(k):
    k = str(n)
    if int(k[-1]) == 0:
        n = n // 10
    else:
        n -= 1
print(n)
