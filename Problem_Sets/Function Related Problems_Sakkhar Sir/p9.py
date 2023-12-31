def multiple(lst):
    newLst = []
    for i in lst:
        newLst.append(i*2)
    return newLst

lst = list(map(int, input().split()))
for x in multiple(lst):
    print(int(x), end=" ")