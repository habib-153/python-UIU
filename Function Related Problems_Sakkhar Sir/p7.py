def onlyEven(lst):
    for i in lst:
        if i%2==0:
            print(i, end=" ")

lst = list(map(int, input().split()))
onlyEven(lst)
# print(lst)