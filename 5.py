def count_numeric(s):
    c=0
    for i in s:
        if i>='0' and i<='9':
            c+=1
    print(c)
s=input()
count_numeric(s)
