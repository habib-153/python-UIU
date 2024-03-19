def ascending(lst):
    sorted = []
    for i in range(len(lst)):
        lowest = min(lst)
        sorted.append(lowest)
        lst.remove(lowest)
    return sorted

lst = list(map(int, input().split()))

result = ascending(lst)
print(" ".join(map(str, result)))