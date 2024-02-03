# listS = ['apple', 'banana', 'kathal', 'aam', 'jaam', 'anaar']
# j = len(listS) - 1
# # print(len(listS))
# # print(j)
# for i in range(0,len(listS)):
#     if (i == j or i!=j) and (i==j+1 or i==j-1):
#         print(listS[j])
#     j=j-1

# ----------------------------------------------------------
# string looping

# test_string = "abc1234"

# for char in test_string:
#     print(chr(ord(char) + 1))

# =============================================
# Looping dictionary
# database = {
#     'abc@gmail.com' : 'abc1234', #bcd2345
#     'gef@gmail.com' : 'bcd4567', #cde5678
#     'qwert@gmail.com' : 'eworig781'
# }

# for key,value in database.items():
#     encoded_password = ""

#     for char in value:

#         if(char == 'z'):
#             encoded_character = 'a'
#         elif(char == 'Z'):
#             encoded_character = 'A'
#         else:
#             encoded_character = chr(ord(char) + 1)

#         encoded_password = encoded_password + encoded_character

#     database[key] = encoded_password

# print(database)

# =========================================================
# PhoneBook

# PhoneBook = {
#     'Amit' :{
#         'NickName' : 'Datto',
#         'Age' : 22,
#         'City' : 'Dhaka'
#     },
#     'Mahera': {
#         'Name': {
#             'First_Name' : 'Mahera',
#             'Last_Name' : 'Rezwan'
#         },
#         'Age': 24,
#         'City': 'Rajshahi'
#     }
# }

# print(PhoneBook)

# ==========================================

# lstCoun = ["Bangladesh", "India", "Pakistan", "Srilanka", "Afganisthan"]
# lstCap = ["Dhaka", "Delhi", "Islamabad" , "Colombo"]

# country = input()

# for c in lstCoun:
#     if(c == country):
#         cap = lstCap[lstCoun.index(c)]
#         print(cap)
#         break

# ===============================================
# my_dict = {'one': 1, 'two':2, 'three': 3}
# a, b, c = my_dict # Unpack keys
# #a, b, c = my_dict.values()
# print(a)
# print(b)

# def make_pizza(*toppings):
#     print(toppings)
# # make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# orginal_lst = [1,2,3,4,5,6]

# def modify_lst(lst):
#     del lst[2]
#     return lst

# output = modify_lst(orginal_lst[:])
# print(f"Original: {orginal_lst}")
# print(f"Modified: {output}")

import math
t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    a = sum(A)
    if int(math.sqrt(a)) * int(math.sqrt(a)) == a:
        print("YES")
    else:
        print("NO")
