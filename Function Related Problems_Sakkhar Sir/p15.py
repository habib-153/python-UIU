def find_substr(a,b):
    if(len(a) > len(b)):
        if b in a:
            return 1
        else:
            return 0
input_str = list(map(str, input().split()))
result = find_substr(input_str[0], input_str[1])
print(result)
    