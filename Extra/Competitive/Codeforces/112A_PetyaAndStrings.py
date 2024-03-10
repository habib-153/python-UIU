# str1 = input()
# str2 = input()

# n_str1 = 0
# n_str2 = 0

# for i in str1:
#     if 65 <= ord(i) <= 90:
#         ordI = ord(i)+ 32
#         n_str1 += ordI
#     else:
#         n_str1 += ord(i)
# for i in str2:
#     if 65 <= ord(i) <= 90:
#         ordI = ord(i)+ 32
#         n_str2 += ordI
#     else:
#         n_str2 += ord(i)   

# if n_str1 < n_str2:
#     print(-1)
# elif n_str1 == n_str2:
#     print(0)
# elif n_str1 > n_str2:
#     print(1)

def compare_strings(string1, string2):
  """Compares two strings lexicographically, ignoring case."""
  lower_string1 = string1.lower()
  lower_string2 = string2.lower()

  # Compare the lowercase versions of the strings
  for i in range(len(string1)):
    if lower_string1[i] < lower_string2[i]:
      return -1
    elif lower_string1[i] > lower_string2[i]:
      return 1

  # If strings are equal up to the end, they are the same
  return 0

string1 = input()
string2 = input()

result = compare_strings(string1, string2)
if result == -1:
  print("-1")
elif result == 1:
  print("1")
else:
  print("0")