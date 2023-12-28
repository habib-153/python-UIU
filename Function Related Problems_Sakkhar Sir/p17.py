def devisor(n):
    lst = [1,n]
    for i in range(2,(n//2)+1):
        if n%i == 0:
            lst.append(i)
    return lst

lst = list(map(int, input().split()))
n1 = devisor(lst[0])
n2 = devisor(lst[1])

def gcd(lst1, lst2):
    common = []
    for i in lst1:
        if i in lst2:
            common.append(i)
    return max(common)

Gcd = gcd(n1, n2)
print(f"GCD: {Gcd}")

lcm = (lst[0]*lst[1]) // Gcd
print(f"LCM: {lcm}")
