def maxe(a):
    max=0
    for i in a:
        if i>max:
            max=i
    print(max)
a=list(map(int,input().split(' ')))
maxe(a)
