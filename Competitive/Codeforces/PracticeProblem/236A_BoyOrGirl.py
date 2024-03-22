name_str = input()
lst = []
for i in name_str:
    if i not in lst:
        lst.append(i)
if len(lst) % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
