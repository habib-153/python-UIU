steps = [5,4,3,2,1]
count = 0

n = int(input())

while n > 0:
    for s in steps:
        if n >= s:
            n-=s
            count += 1
            break
print(count)