finish_time_str = input().split()
finish_time = [int (x) for x in finish_time_str]
copy = finish_time.copy()
# print(copy)
min_sorted = sorted(copy)
winner =[]
# print(min_sorted)
for i in range(0,3):
    idx = finish_time.index(min_sorted[i])
    winner.append(idx)
print(f"First Place: {winner[0]}")
print(f"Second Place: {winner[1]}")
print(f"Third Place: {winner[2]}")