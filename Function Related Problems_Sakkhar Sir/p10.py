def sort_ascending(lst):
    sorted_array = sorted(lst)
    return sorted_array

lst = list(map(int, input().split()))

result = sort_ascending(lst)
print(" ".join(map(str, result)))