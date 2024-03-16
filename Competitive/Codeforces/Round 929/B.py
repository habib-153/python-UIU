def minMoves(arr, n):
    S = sum(arr)
    rem = S % 3
    if rem == 0:
        return 0
    elif rem == 1:
        # Find the smallest element with remainder 1
        arr.sort()
        for num in arr:
            if num % 3 == 1:
                return 1
        return 2  # If no element with remainder 1, we need to add 2 to an element
    else:  # rem == 2
        # Find the smallest element with remainder 2
        arr.sort()
        count = 0
        for num in arr:
            if num % 3 == 2:
                return 1
            elif num % 3 == 1:
                count += 1
                if count == 2:
                    return 1
        return 2
# Example usage
t = int(input())
lst= []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    lst.append(minMoves(arr, n))

for i in lst:
    print(i)

