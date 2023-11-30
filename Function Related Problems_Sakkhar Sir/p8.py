def minimum(lst):
    lst.sort()
    # print(lst)
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    print("Minimum Value: ",min_value)

lst = list(map(int, input().split()))
minimum(lst)