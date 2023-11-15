
# num = [1, 2, 3, 4, 4, 5]

# for n in num:
#     if (n == 4):
#         remove:(n)
#     else:
#         print(n)
# motor = ['honda', 'yamaha', ['kawasaki', 'bajaj'], 'sujuki', 'hero']
# print(sorted(motor, key=str))


# motor = ["honda", "yamaha", ["kawasaki", "bajaj"], "suzuki", "hero"]
# for i in range (len (motor)):
#   if isinstance (motor [i], list):
#     motor [i].sort ()
# motor.sort (key=lambda x: x [0] if isinstance (x, list) else x)
# print (motor)

# motor = ["honda", "yamaha", ["kawasaki", "bajaj"], "suzuki", "hero"]
# sorted_motor = [sorted (x, key=str) if isinstance (x, list) else x for x in motor]
# sorted_motor = sorted (sorted_motor, key=str)
# print(sorted_motor)
# ---------------------------------------------------------

    # N = int(input())
    #     # Initialize a variable to store the sum
    # sum = 0
    #     # Loop from 1 to N
    # for i in range(1, N + 1):
    #     # using formula....
    #     term = i * (-1) ** i
    #         # Add the term to the sum
    #     # print(term)
    #     sum += term
    #     # Print the sum
    # print(sum)
    # # print(term)

# -------------------------------------------------------
# num = int (input())
# if(num+1)%2 == 1:
#     index_value = num+1
# else:
#     index_value = -(num+1)
# print(index_value)
# -------------------------------------------------------

# start = int(input())
# end = int(input())
# list =[]
# for i in range(start, end+1):
#     if i%2 == 0:
#         list.append(i)
# print(list)
# -------------------------------------------------------
# x=0
# for i in range(1,4):
#     for j in range(1,4):
#         x+=i
#         if x>j:
#             continue
#         print(f"{i} {j}")
# --------------------------------------------------------------
# word="I Love Bangladesh"
# i=0
# while i<len(word):
#    if word[i].lower()=='l'.lower() or word[i].lower()=='o'.lower():
#         i=i+1
#         continue
#    else:
#         print(word[i], end=',')
#         i=i+1
# ----------------------------------------------------
# not print coma after last element
# n = 5
# lst = []
# while n<= 100:
#     lst.append(str(n))
#     n+=10
# print(",".join(lst))
# -------------------------------------------------------

# palindrome
    # input_str = input()

    # reversed_str = "".join(reversed(input_str))
    # # print(input_str)
    # # print(reversed_str)
    # if input_str.lower() == reversed_str.lower():
    #     print("palindrome")
    # else:
    #     print("not palindrome")

# -----------------------------------------------------
