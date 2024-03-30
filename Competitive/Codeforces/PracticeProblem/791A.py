lst_input = list(map(int, input().split()[:2]))
m =  lst_input[0]
n = lst_input[1]

count = 0

while m <= n:
    count += 1
    m = m*3
    n = n*2

print(count)