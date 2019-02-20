def count_sc(s):
    a=[',','!','@','#','$','^','&','.',':',';','`','~']
    c=0
    for i in s:
        if i in a:
            c+=1
    print(c)
s=input()
count_sc(s)
    
