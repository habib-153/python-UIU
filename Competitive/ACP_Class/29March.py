n = int(input())

lst_num = []
for i in range(n):
    coordinates = tuple(map(int, input().split()))
    lst_num.append(coordinates)

def sort_by_coordinates(coord):
    x, y = coord
    return (x, -y)

sorted_list = sorted(lst_num, key=sort_by_coordinates)

print(sorted_list)
