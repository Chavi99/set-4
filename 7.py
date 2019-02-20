def swap_num(a,b):
    b,a=a,b
    print(a,b)
x=list(map(int,input().split(' ')))
swap_num(x[0],x[1])
