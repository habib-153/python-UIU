# def isPrime(n):
#     if n <=1:
#         return False
#     for i in range(2, (n//2)+1):
#         if n % i == 0:
#             return False
#     return True
from p11 import isPrime
def GeneratePrime(n):
    lst = []
    for i in range(n):
        if isPrime(i):
            lst.append(i)
    return lst

num = int(input())
print(f"Prime less than {num}: {' '.join(map(str, GeneratePrime(num)))}")
