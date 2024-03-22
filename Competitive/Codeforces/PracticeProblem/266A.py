n = int(input())
str_input = input()[:n]
count = 0
for i in range(len(str_input) - 1):
    if str_input[i] == str_input[i+1]:
        count += 1
print(count)