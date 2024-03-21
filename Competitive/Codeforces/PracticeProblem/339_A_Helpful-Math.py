str_input = input()
lst = list(map(int, str_input.split("+")))
sorted_str_lst = [str(num) for num in sorted(lst)]
print("+".join(sorted_str_lst))