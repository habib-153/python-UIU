str_input = input()
if str_input[0].islower():
    new_str = str_input[0].capitalize() + str_input[1:]
    print(new_str)
else:
    print(str_input)