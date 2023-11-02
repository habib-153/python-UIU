listS = ['apple', 'banana', 'kathal', 'aam', 'jaam', 'anaar']
j = len(listS) - 1
# print(len(listS))
# print(j)
for i in range(0,len(listS)):
    if (i == j or i!=j) and (i==j+1 or i==j-1):
        print(listS[j])
    j=j-1