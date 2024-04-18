def min_operations_to_non_decreasing(arr):
    n = len(arr)
    # Initialize the count of operations to 0
    count = 0
    # Start from the second element and go up to the last
    for i in range(1, n):
        # If the current element is less than the previous one
        if arr[i] < arr[i - 1]:
            # Calculate the number of operations needed
            operations = (arr[i - 1] - arr[i] + arr[i] - 1) // arr[i]
            # Add the operations to the count
            count += operations
            # Increase the current element by the total value added
            arr[i] += operations * arr[i]
    return count

# Example usage:
print(min_operations_to_non_decreasing([4, 3, 2, 7, 6, 9]))  # Output should be 2
print(min_operations_to_non_decreasing([55, 50, 87, 17, 36, 90, 6]))  # Output should be 4
print(min_operations_to_non_decreasing([55, 50, 87, 17, 36, 90, 6, 74, 67, 92, 40, 18, 97, 78, 86, 41, 88]))  # Output should be 10