list_str = input().split()
list = [int (x) for x in list_str]
list.sort()
max = list[0]
for i in list:
    if i > max:
        max = i
print(max)