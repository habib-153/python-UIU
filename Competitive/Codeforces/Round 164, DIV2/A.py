for _ in range(int(input())):
    n,m,k=[*map(int,input().split())]
    print(["NO","YES"][not(n<=k or k>=(n//m)*(m-1)+(n%m!=0)*(n%m-1))])

# wrong ans on test case 2