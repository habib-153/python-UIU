def swap(lst):
    lst[0], lst[1] = lst[1], lst[0]
    print(f"Value in func: {lst[0]} {lst[1]}")

n1 ,n2 = map(int,input().split())

lst = [n1, n2]
swap(lst)
print(f"Value in main: {lst[0]} {lst[1]}")