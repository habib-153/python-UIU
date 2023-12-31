def Get_Number_And_Base():
    lst = list(map(int, input().split()))
    N = lst[0]
    B = lst[1]
    return (N, B)

def Convert_Number(N, B):
    result = ""
    digits = "0123456789ABCDEF"
    while N > 0:
        rem = N % B
        # result = str(rem) + result
        result = digits[rem] + result
        N = N // B
    return result

def Show_Converted_Number(result):
    print(f"{result}")

# Main function
if __name__=="__main__":
    N, B = Get_Number_And_Base()
    if B < 2 or B > 16:
        print("Base not within proper range!")
    else:
        result = Convert_Number(N, B)
        Show_Converted_Number(result)
