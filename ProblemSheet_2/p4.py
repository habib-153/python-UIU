# Ask the user to enter the number of inputs
# N = int(input())
# numbers = []

# for i in range(N):
#     num = float(input())
#     numbers.append(num)

# total = sum(numbers)
# average = total / N

# print("Average: {:.4f}".format(average))

# n = int(input())
# number = input().split()[:n]
# sum = 0
# for i in number:
#     sum = sum + float(i)
# avg = sum / n
# print(avg)


N = int(input("Enter the number of inputs: "))

# Get a list of strings from the input by splitting on spaces
numbers = input("Enter the numbers in one line: ").split()

# Convert the strings to floats using map
numbers = list(map(float, numbers))

# Check if the number of inputs matches N
if len(numbers) != N:
    print("Invalid input")
else:
    # Calculate the sum of the numbers in the list
    total = sum(numbers)

    # Calculate the average by dividing the sum by N
    average = total / N

    # Print the average with four decimal places
    print("Average: {:.4f}".format(average))