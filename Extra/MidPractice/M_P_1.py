char = input()

if 65 <= ord(char) < 97:
    print(chr(ord(char) + 32))
else: 
    print(chr(ord(char) - 32))
# else:
#     print("Result:", char)
print(ord(char))