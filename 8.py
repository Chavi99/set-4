def swap_n(x,y):
    x=x^y
    y=x^y
    x=x^y
    print(x,y)
n=list(map(int,input().split(' ')))
swap_n(n[0],n[1])
