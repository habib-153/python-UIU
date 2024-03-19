list_str = input().split()
list =[int (x) for x in list_str]

sum_of_odd = 0
sum_of_even = 0
if len(list)==1:
    print('can not possible')

for i in list:
    if list.index(i) % 2 == 0:
        sum_of_even = sum_of_even + i
    elif list.index(i) % 2 == 1:
        sum_of_odd = sum_of_odd + i
print(f"Even index {sum_of_even}")
print(f"Odd Index {sum_of_odd}")
                                                    