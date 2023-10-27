n = int(input("Enter a number: "))

reverse = ""
remainder = 0
# zero hoa porjonto loop chalabo e jonno while loop
while n > 0:
  remainder = n % 10
  reverse += str(remainder) + ""
  n = n // 10
print(reverse)