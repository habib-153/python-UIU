n = int(input())

reverse = ""
remainder = 0
# zero na hole loop chalabo e jonno while loop
while(n > 0):
    remainder = n % 10
    reverse += str(remainder) + ""
    n = n // 10
print(reverse)