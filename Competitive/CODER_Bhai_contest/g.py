def f(x):
    enclosed_areas = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
    result = 0
    while x > 0:
        digit = x % 10
        result += enclosed_areas[digit]
        x //= 10
    return result
def g_k(x, k):
    for _ in range(k):
        x = f(x)
    return x

T = int(input())
lst = []
for _ in range(T):
    x, k = map(int, input().split())
    lst.append(g_k(x, k))
for i in lst:
    print(i)
