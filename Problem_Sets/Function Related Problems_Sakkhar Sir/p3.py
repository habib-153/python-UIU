def calculateSum(list):
    total = sum(list)
    print(f"Sum In Function: {total}")
    print(f"Sum In Main: {total}")

lst_str = input().split()
lst = [int (x) for x in lst_str]
calculateSum(lst)