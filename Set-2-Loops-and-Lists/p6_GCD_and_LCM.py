numbers = input().split()
num = [int(x) for x in numbers]
if len(num)==2:
    x=num[0]
    y=num[1]
    for i in range(max(x,y)):
        if y == 0:
            break
        temp = x
        x = y
        y = temp
        y= y%x
        print(f":{y}")
    gcd = x
    lcm = (num[0]*num[1])//gcd
    print(gcd)
    print(lcm)
