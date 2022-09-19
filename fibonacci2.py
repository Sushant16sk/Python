#fibonacci series using recursion
def fibo(n):
    if n<=1:
        return n;
    else:
        return(fibo(n-1)+fibo(n-2))
n=int(input('enter number of elements in series: '))
if n<=0:
    print('enter a positive number')
else:
    for i in range(n):
        print(fibo(i))