def ShowMatrix(mat):
    """Disply the original matrix"""
    print(f"Original:")
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()

def ScalarMultiply(mat, n):
    print(f"Multiplied by {n}: ")
    for i in mat:
        for j in i:
            k = j*n
            print(k, end="\t")
        print()
def InputMatrix():
    """Take inupt for the matrix from the user"""
    for i in range(3):
        user_input = input().split()
        lst = [int(x) for x in user_input][:5]
        matrix.append(lst)
if __name__=="__main__":

    matrix = []

    first_call = InputMatrix()

    num = int(input("\n"))

    diplay = ShowMatrix(matrix)
    multiply = ScalarMultiply(matrix, num)