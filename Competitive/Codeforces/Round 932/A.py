# t = int(input())   
# lst = []
# for _ in range(t):
#     n = int(input())  
#     s = input().strip()

#     for i in range(n):
#         s = s[::-1]
#     lst.append(s)
# for i in lst:
#     print(i)

def lexsmall(s, n):
    # Check if the input is valid
    if not isinstance(s, str) or not isinstance(n, int):
        return s
    if n % 2 != 0 or n < 2:
        return s
    
    # Initialize the new string variable
    new_s = s

    # Loop n times and apply the operations
    for i in range(n):
        # Check the type of operation
        if i % 2 == 0: # First type of operation
            # Add the reversed string to the end of the new string
            new_s = new_s + new_s[::-1]
        else: # Second type of operation
            # Reverse the new string
            new_s = new_s[::-1]
        
        # Compare the new string with the original string and keep the lexicographically smaller one
        if new_s > s:
            new_s = s
    
    # Return the new string
    return new_s
t = int(input())   
lst = []
for _ in range(t):
    n = int(input())  
    s = input().strip()
    new_str = lexsmall(s, n)
    lst.append(new_str)
for i in lst:
    print(i)
