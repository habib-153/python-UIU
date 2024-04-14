s= input()
upper = sum(1 for i in s if i.isupper())
lower = sum(1 for i in s if i.islower())
# if lower > upper:
#     print(s.lower())
if upper > lower:
    print(s.upper())
else:
    print(s.lower())