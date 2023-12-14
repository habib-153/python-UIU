def isPrime(n):
    if n <=1:
        return False
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True

def GenNthPrime(num):
    lst = [2]
    count = 1
    i = 3
    while count < num :
        if isPrime(i):
            lst.append(i)
            count += 1
        i += 2
    return lst

number = int(input())
print(f"{number}th Prime: {GenNthPrime(number)[-1]}")