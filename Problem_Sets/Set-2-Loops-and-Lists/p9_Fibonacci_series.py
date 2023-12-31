fibo_series =[1,1]
fibo =[]
N = int(input())
for i in range(2,N):
    i = fibo_series[i-1]+fibo_series[i-2]
    fibo_series.append(i)
for fibo in range(0,N):
    print(fibo_series[fibo], end=' ')
