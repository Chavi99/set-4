def fib(n):
    c1=0
    c2=1
    print(1,end=" ")
    n-=1
    while n>0:
        c3=c1+c2
        print(c3,end=" ")
        c1=c2
        c2=c3
        n-=1
n=int(input())
fib(n)
