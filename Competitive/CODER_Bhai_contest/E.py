N, M = map(int, input().split())

items = set()

for _ in range(N):
    item = input()
    items.add(item)

count = 0

for i in range(M):
    T_i = int(input())
    required_items = set()
    for j in range(T_i):
        required_item = input()
        required_items.add(required_item)
    if required_items.issubset(items):
        count += 1
print(count)