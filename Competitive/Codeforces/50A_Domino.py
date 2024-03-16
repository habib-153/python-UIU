lst = list(map(int, input().split()[:2]))
m = lst[0]
n = lst[1]

sq = m * n

max_domino = sq // 2

print(max_domino)