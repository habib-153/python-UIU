def ScalarMultiply(matri, n):
    """Multiply the matrix with the inputed number."""
    print(f"\nMultiplied by {n}:")
    for i in matri:
        for j in i:
            x = j*n
            print(x, end="\t")
        print()

def ShowMatrix(mat):
    """Disply the original matrix"""
    print(f"\nOriginal:")
    for i in mat:
        for j in i:
            print(j, end="\t")
        print()

def InputMatrix(row_num, column_num):
    """Take inupt for the matrix from the user"""
    print(f"\nEnter the matrix:")
    for i in range(row_num):
        user_input = input().split()
        lst = [int(x) for x in user_input]
        if len(lst) != column_num:
            print("Input Error! Rerun the program!!!")
        matrix.append(lst)
    
matrix = []
lst = list(map(int, input("Enter the dimention of the matrix: (Row Column)\n").split()))

row = lst[0]
column = lst[1]

first_call = InputMatrix(row_num=row, column_num=column)

num = int(input("\nMultiply by:\n"))

diplay = ShowMatrix(matrix)
multiply = ScalarMultiply(matri=matrix, n=num)