n = int(input()) 
c = int(input())
initial_heights = list(map(int, input().split()[:n])) 

new_heights = [height + 2 * c for height in initial_heights]

for height in new_heights:
    print(height, end=" ")