n = int(input())
lst_input = list(map(int, input().split()[:n]))

if len(set(lst_input)) == 1:
    print("Yes")
else:
    print("No")