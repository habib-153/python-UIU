# Ask the user to enter the number of inputs
# N = int(input())
# numbers = []

# for i in range(N):
#     num = float(input())
#     numbers.append(num)

# total = sum(numbers)
# average = total / N

# print("Average: {:.4f}".format(average))

n = int(input())
number = input().split()[:n]
sum = 0
for i in number:
    sum = sum + float(i)
avg = sum / n
print("Average: {:.4f}".format(avg))
