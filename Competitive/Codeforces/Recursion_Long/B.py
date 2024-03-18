import math

lst = []
try:
    while True:
        n= input()
        lst+= list(map(int,n.split()))
except EOFError:
    pass

for i in lst[::-1]:
    number = math.sqrt(i)
    print(f"{number:.4f}")
