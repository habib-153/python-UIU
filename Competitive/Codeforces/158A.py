lst1 = list(map(int, input().split()[:2]))
n = lst1[0]
k = lst1[1]
count =0

lst2 = list(map(int, input().split()[:n]))

for i in lst2:
    if i > 0 and i >= lst2[k-1]:
        count += 1
print(count)